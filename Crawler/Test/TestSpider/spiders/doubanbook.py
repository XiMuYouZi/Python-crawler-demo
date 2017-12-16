import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from Test.TestSpider.items import DoubanItem
from scrapy.shell import inspect_response
from scrapy import shell



class DoubanDemoSpider(CrawlSpider):
    name = "douban_book"
    allowed_domains = ["douban.com"]
    start_urls = ['https://book.douban.com/tag']
    rules={
        Rule(LinkExtractor(allow='/tag/',restrict_xpaths="//div[@class='article']"),follow=True),
        Rule(LinkExtractor(allow="\?start=\d+\&type=",restrict_xpaths="//div[@class='paginator']"),follow=True),
        Rule(LinkExtractor(allow="/subject/\d+/$",restrict_xpaths="//ul[@class='subject-list']"),callback='parse_item')
    }
    def parse_item(self,response):
        item=DoubanItem()
        if response.status==200:
            #inspect_response(response,self)
            try:
                item['name']=response.xpath("//div[@id='wrapper']/h1/span/text()").extract()[0]
                item["author"]=response.xpath("//div[@id='info']/a[1]/text()")[0].extract()
                item['pingjia']=response.xpath("//div[@class='rating_self clearfix']/strong/text()")[0].extract()
                content=response.xpath("//div[@class='intro']//p/text()").extract()
                author_jianjie=response.xpath("//div[@class='intro']//p/text()").extract()
                item['content']=""
                item['author_jianjie']=""
                for p in content:
                    item['content']=item['content']+p
                for jianjie in author_jianjie:
                    item["author_jianjie"]=item['author_jianjie']+jianjie
                yield item
            except:
                print ("------------------------------------------error-----------------------------------------")
        else:
            print ('**********************************************************************************************')
