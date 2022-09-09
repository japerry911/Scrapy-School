from scrapy import Field, Item


class EbookItem(Item):
    title = Field()
    price = Field()
