import scrapy
from scrapy.loader import ItemLoader

from ebook_scraper.items import EbookItem


class EbookSpider(scrapy.Spider):
    name = "ebook"
    # start_urls = ["https://books.toscrape.com/"]
    start_urls = [
        # "https://books.toscrape.com/catalogue/category/books/travel_2",
        "https://books.toscrape.com/catalogue/category/books/mystery_3"
    ]
    cols = ["Title", "Price"]

    def __init__(self):
        super().__init__()
        self.page_count = 0

    def parse(self, response: scrapy.http.Response, **_kwargs):
        self.page_count += 1

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

        print(f"[ PAGE COUNT ]: {self.page_count}")

        next_btn = response.css("li.next a")

        if next_btn:
            next_page = f"{self.start_urls[0]}/{next_btn.attrib['href']}"

            yield scrapy.Request(url=next_page)
