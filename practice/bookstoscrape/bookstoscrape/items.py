from itemloaders.processors import MapCompose, TakeFirst
from scrapy import Field, Item


def get_price_amount(txt: str) -> float:
    return float(txt.replace("£", ""))


def convert_to_usd_dollars(pounds: float) -> float:
    return pounds * 0.89


class EbookItem(Item):
    title = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(
            get_price_amount,
            convert_to_usd_dollars
        ),
        output_processor=TakeFirst()
    )
