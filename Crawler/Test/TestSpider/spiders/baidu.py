# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader.processors import *
from w3lib.html import remove_tags
from scrapy.loader import ItemLoader


def filter_price(value):
    if value.isdigit():
        return value

class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()
    name_in = MapCompose(remove_tags)
    name_out = Join()
    price_in = MapCompose(remove_tags,filter_price)
    price_out = TakeFirst()


class ProductItem(scrapy.Item):
    name = scrapy.Field(
        # input_processor=MapCompose(remove_tags),
        # output_processor=Join(),
    )
    price = scrapy.Field(
        # input_processor=MapCompose(remove_tags, filter_price),
        # output_processor=TakeFirst(),
    )


il = ProductLoader(item=ProductItem())
il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
il.add_value('price', [u'XXXX', u'<span>1000</span>'])
print(il.load_item())


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        print('start_requests调用')
        yield Request(url='http://www.qq.com',callback=self.index_parse)
    #
    #
    def make_requests_from_url(self, url):
        print('make_requests_from_url调用')
        return Request(url='http://www.12306.cn',meta={'download_timeout':10}, callback=self.parse)
    #
    #
    def index_parse(self,response):
        print('index_parse: ', response)

    def parse(self, response):
        print('parse: ', response)
