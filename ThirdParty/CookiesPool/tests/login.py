import requests
from bs4 import BeautifulSoup
from Crawler.haixinSpider.parseHtml import *
from ThirdParty.CookiesPool.cookiespool.db import *
import json


cookie_client = CookiesRedisClient(name='weibo')
cookie1 = json.loads(cookie_client.random())
for page in range(1,10):
    url = 'https://weibo.cn/u/1786213845?page={}'.format(page)
    print(url)
    print(parseHtml().getStaticHtmlConten(url=url  , cookies=cookie1,headers=''))

