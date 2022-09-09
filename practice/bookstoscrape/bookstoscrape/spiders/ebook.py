from scrapy import http, Spider

from bookstoscrape.items import EbookItem


class EbookSpider(Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def __init__(self):
        super().__init__()
        self.page_count = 0

    def parse(
            self,
            response: http.Response,
            **_kwargs
    ):
        self.page_count += 1

        ebooks = response.css("article.product_prod")

        for ebook in ebooks:
            ebook_item = EbookItem()

            title = ebook.css("h3 a").attrib["title"]
            price = ebook.css("div.product_price p.price_color::text").get()

            ebook_item["title"] = title
            ebook_item["price"] = price

            yield ebook_item
