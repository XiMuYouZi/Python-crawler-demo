# -*- coding: utf-8 -*-
import scrapy
import re
from  pyquery import PyQuery as pq
from dingdian.dingdian.items import DingdianItem
from scrapy.http import Request

class DingdianxiaoshuoSpider(scrapy.Spider):
    name = 'dingdianxiaoshuo'
    allowed_domains = ['x23us.com']
    # start_urls = ['http://www.x23us.com//class/']
    base_url = 'http://www.x23us.com/class/'
    suffix = '.html'


# 获取每个分类的初始URL
    def start_requests(self):
        for i in range(1,11):
            url = self.base_url + str(i) + '_1' + self.suffix
            yield  Request(url=url, callback=self.parse)
        yield Request(url='http://www.x23us.com/quanben/1', callback=self.parse)


#获取每个分类下面的全部页面的URL
    def parse(self, response):
        responseText = pq(response.text)
        g1 = list(responseText('#pagelink > a.last ').items())
        baseURL = str(response.url)[:-6]
        max_num = g1[0].text()
        for num in range(1,int(max_num)+1):
            url = baseURL + str(num) + self.suffix
            yield Request(url = url, callback=self.getName)


#获取每个分类下面的每个页面的每个小说名字和链接
    def getName(self,response):
        content = pq(response.text)
        g1 = list(content('#content > dd:nth-child(2) > table [bgcolor="#FFFFFF"] > td:nth-child(1) > a:nth-child(1)' ).items())
        for item in g1:
            name = item.attr('title')
            url = item.attr('href')
            yield Request(url=url,callback=self.get_novel_info,meta={'name':name,'url':url})



#获取每个小说的信息
    def get_novel_info(self,response):
        htmlContent = pq(response.text)
        item = DingdianItem()
        name = str(response.meta['name'])[:-2]
        url = str(response.meta['url'])
        cover = "http://www.x23us.com" + htmlContent('#content > dd:nth-child(3) > div:nth-child(1) > a > img').attr('src')
        category = htmlContent.find('table').find('td').eq(0).text()
        author = htmlContent.find('table').find('td').eq(1).text()
        status = htmlContent.find('table').find('td').eq(2).text()
        collect_num = htmlContent.find('table').find('td').eq(3).text()
        content_len = htmlContent.find('table').find('td').eq(4).text()
        last_refresh_time = htmlContent.find('table').find('td').eq(5).text()
        desc = htmlContent.find('dd').eq(3).find('p').eq(1).text()
        nameID = htmlContent.find('.read').attr('href')[-6:-1]
        item['nameID'] = nameID
        item['name'] = name
        item['url'] = url
        item['cover'] = cover
        item['author'] = author
        item['collect_num'] = collect_num
        item['content_len'] = content_len
        item['last_refresh_time'] = last_refresh_time
        item['desc'] = desc
        item['category'] = category
        item['status'] = status
        return item

