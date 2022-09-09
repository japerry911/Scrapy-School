import scrapy

from ebook_scraper.items import EbookItem


class EbookSpider(scrapy.Spider):
    name = "ebook"

    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response: scrapy.http.Response, **_kwargs):
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            ebook_item = EbookItem()

            ebook_item["title"] = ebook.css("h3 a").attrib["title"]
            # shorter example: title = ebook.css("h3 a::attr(title)").get()
            ebook_item["price"] = ebook.css(
                "div.product_price p.price_color::text"
            ).get()

            yield ebook_item
