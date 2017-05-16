# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

class YangzieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass




class LagouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


# 去掉城市名两边的斜线
def remove_sp(value):
    return value.replace("/", "")

class LagouItem(scrapy.Item):
    url = scrapy.Field()
    url_id = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field(
        input_processor = MapCompose(remove_sp)
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_sp)
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_sp)
    )
    types = scrapy.Field(
        input_processor=MapCompose(remove_tags)
    )
    publish_time = scrapy.Field()
    tags = scrapy.Field(
       # input_processor = Join(",")
    )
    descs = scrapy.Field()
    address = scrapy.Field(
        input_processor = MapCompose(remove_tags)
    )
    company_url = scrapy.Field()
    company_name = scrapy.Field()
    created_at = scrapy.Field()














