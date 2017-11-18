# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    nameID = scrapy.Field()
    category = scrapy.Field()
    status = scrapy.Field()
    cover = scrapy.Field()
    collect_num = scrapy.Field()
    content_len = scrapy.Field()
    last_refresh_time = scrapy.Field()
    desc = scrapy.Field()


