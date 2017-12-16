# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#小说概览信息
class novelInfoItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    novelID = scrapy.Field()
    category = scrapy.Field()
    status = scrapy.Field()
    file_urls = scrapy.Field()
    files =scrapy.Field()
    collect_num = scrapy.Field()
    content_len = scrapy.Field()
    last_refresh_time = scrapy.Field()
    desc = scrapy.Field()


#每篇小说的章节信息
class novelChapterInfoItem(scrapy.Item):
    novelID = scrapy.Field()
    content = scrapy.Field()
    serialNum = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()


