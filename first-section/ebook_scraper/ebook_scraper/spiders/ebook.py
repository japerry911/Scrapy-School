import scrapy
from scrapy.loader import ItemLoader

from ebook_scraper.items import EbookItem


class EbookSpider(scrapy.Spider):
    name = "ebook"

    # start_urls = ["https://books.toscrape.com/"]
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/travel_2/"
    ]

    def parse(self, response: scrapy.http.Response, **_kwargs):
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            loader = ItemLoader(
                item=EbookItem(),
                selector=ebook
            )
            # ebook_item = EbookItem()

            loader.add_css("title", "h3 a::attr(title)")
            # ebook_item["title"] = ebook.css("h3 a").attrib["title"]
            # shorter example: title = ebook.css("h3 a::attr(title)").get()
            loader.add_css(
                "price",
                "div.product_price p.price_color::text"
            )
            # ebook_item["price"] = ebook.css(
            #     "div.product_price p.price_color::text"
            # ).get()

            # yield ebook_item
            yield loader.load_item()
