import scrapy


class EbookSpider(scrapy.Spider):
    name = "ebook"

    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response: scrapy.http.Response, **_kwargs):
        print("[ parse ]")

        response.css("h3 a::text")
        response.xpath("//h3/a/text()")
