from scrapy import http, loader, Spider

from bookstoscrape.items import EbookItem


class EbookSpider(Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com"]

    def __init__(self):
        super().__init__()
        self.page_count = 0

    def parse(
            self,
            response: http.Response,
            **_kwargs
    ):
        self.page_count += 1

        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            item_loader = loader.ItemLoader(
                item=EbookItem(),
                selector=ebook
            )

            item_loader.add_css(
                "title",
                "h3 a::attr(title)"
            )
            item_loader.add_css(
                "price",
                "div.product_price p.price_color::text"
            )

            yield item_loader.load_item()
