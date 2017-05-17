# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags
import re

from scrapy.loader.processors import Join

class YangzieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass




class LagouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


# 去掉城市名两边的斜线
def remove_sp(value):
    return value.replace("/", "")
# 去掉 \n

def remove_n(value):
    return value.replace('\n', "")

# 去掉space
def remove_space(value):
    return value.replace(" ", "")

def get_default(value):
    return value

# 查看地图
def remove_map(value):
    if re.match('.*(查看地图).*', value):
        return value.replace('查看地图', '')





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
        # input_processor = MapCompose(list_to_str),
        output_processor=Join(separator=u' ')
    )
    descs = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_n, remove_space)
    )
    address = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_n, remove_space, remove_map)
    )
    company_url = scrapy.Field()
    company_name = scrapy.Field()
    created_at = scrapy.Field()














