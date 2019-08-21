# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AstockItem(scrapy.Item):
    # define the fields for your item here like:
    astock_id = scrapy.Field()
    astock_name = scrapy.Field()
    date = scrapy.Field()
    volume = scrapy.Field()
    open = scrapy.Field()
    close = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
