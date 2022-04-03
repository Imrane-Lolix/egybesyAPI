from egy_best.lib.utils import Utils
from egy_best.lib.translator import Translator
from cached_properties import Property as property


class Home:
    def __init__(self):
        self.link = Utils.make_link()
        for name, value in self.scrape_home_page().items():
            setattr(self, name, value)

    def shows_container_scrape(self, item):
        t = item.find(class_='contents movies_small')
        return [Utils.pickup_class(
                link=item['href'],
                title=item.find(class_='title').text,
                thumbnail=item.img['src']
                )
                for item in t.find_all('a')]

    def scrape_home_page(self):
        big_con = self.soup.find(id='mainLoad')
        return {Translator.translate(item.div.strong.text.strip()): self.shows_container_scrape(item)
                for item in big_con.find_all(class_='mbox')
                if item.a}

    @property(general=True, timeout=86400)
    def soup(self):
        return Utils.page_downloader(self.link)
