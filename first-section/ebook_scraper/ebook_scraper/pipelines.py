import os
from typing import Optional

from itemadapter import ItemAdapter
# from openpyxl import Workbook
from pymongo import collection, MongoClient

from ebook_scraper.spiders.ebook import EbookSpider


class EbookScraperPipeline:
    def __init__(self):
        self.workbook = None
        self.sheet = None
        self.client: Optional[MongoClient] = None
        self.collection: Optional[collection.Collection] = None

    def open_spider(self, spider: EbookSpider):
        # self.workbook = Workbook()
        # self.sheet = self.workbook.active
        # self.sheet.title = "ebooks"
        #
        # self.sheet.append(spider.cols)
        self.client = MongoClient(
            host=f"mongodb+srv://Skylord:{os.getenv('MONGODB_PASS')}@"
                 "ebookscraper.hkxpmns.mongodb.net/?retryWrites=true&w="
                 "majority",
            connect=False
        )
        self.collection = self.client.get_database(
            "EbookScraper"
        ).get_collection("travel")

    def process_item(self, item, _spider: EbookSpider):
        # self.sheet.append([item["title"], item["price"]])
        self.collection.insert_one(
            ItemAdapter(item).asdict()
        )

        return item

    def close_spider(self, _spider: EbookSpider):
        # self.workbook.save("tmp_output.xlsx")
        self.client.close()
