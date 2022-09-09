from scrapy import http, Spider


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
            title = ebook.css("h3 a::attr(title)").get()
            price = ebook.css("div.product_price p.price_color::text").get()

            print(title)

            yield {
                "title": title,
                "price": price
            }
