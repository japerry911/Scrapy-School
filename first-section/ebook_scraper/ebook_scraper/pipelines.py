from openpyxl import Workbook
from ebook_scraper.spiders.ebook import EbookSpider

class EbookScraperPipeline:
    def __init__(self):
        self.workbook = None
        self.sheet = None

    def open_spider(self, spider: EbookSpider):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "ebooks"

        self.sheet.append(spider.cols)

    def process_item(self, item, _spider: EbookSpider):
        self.sheet.append([item["title"], item["price"]])

    def close_spider(self, _spider: EbookSpider):
        self.workbook.save("tmp_output.xlsx")
