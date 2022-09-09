from scrapy import Field, Item
from itemloaders.processors import MapCompose, TakeFirst


def get_price(txt: str) -> float:
    return float(txt.replace("£", ""))


def convert_to_usd_dollars(pounds: float) -> float:
    return pounds * 0.89


class EbookItem(Item):
    title = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(
            get_price,
            convert_to_usd_dollars
        ),
        output_processor=TakeFirst()
    )
