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
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/']


    def __init__(self,mongo_uri,mongo_db, *args , **kwargs):
        super(BaiduSpider,self).__init__(*args,**kwargs)
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        return cls(
            mongo_uri=crawler.settings.get('mongo_uri'),
            mongo_db=crawler.settings.get('mongo_db')
        )

    # def start_requests(self):
    #     yield Request(url='http://www.qq.com',callback=self.index_parse)

    def make_requests_from_url(self, url):
        yield Request(url='http://www.sina.com', callback=self.parse)


    def index_parse(self,response):
        print('11111',response)

    def parse(self, response):
        print('222222',response)
