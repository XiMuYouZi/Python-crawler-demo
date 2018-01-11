# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
import logging
import requests
from requests.exceptions import ConnectionError
from scrapy.exceptions import IgnoreRequest


class CookiesMiddleWare():
    def __init__(self, cookies_pool_url):
        self.logger = logging.getLogger(__name__)
        self.cookies_pool_url = cookies_pool_url

    def _get_random_cookies(self):
        try:
            #先开启cookie_pool的python项目，使用flask提供cookie
            response = requests.get(self.cookies_pool_url)
            if response.status_code == 200:
                return json.loads(response.text)
        except ConnectionError:
            return None

    def process_request(self, request, spider):
        cookies = self._get_random_cookies()
        if cookies:
            request.cookies = cookies
            self.logger.debug('Using Cookies ' + json.dumps(cookies))
        else:
            self.logger.debug('No Valid Cookies')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies_pool_url=crawler.settings.get('COOKIES_POOL_URL')
        )

#处理页面重定向问题
    def process_response(self, request, response, spider):
        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers['location']
                #重定向到登录界面，说明cookie失效了，需要重新获取该账号的cookie
                if 'login.weibo' in redirect_url or 'login.sina' in redirect_url:  # Cookie失效
                    self.logger.warning('Updating Cookies')
                #重定向到账号解封页面，说明账号被封了
                elif 'weibo.cn/security' in redirect_url:
                    self.logger.warning('Now Cookies' + json.dumps(request.cookies))
                    self.logger.warning('One Account is locked!')
                #返回一个新的request对象，并且重新设置cookie，此时中间件链停止， 返回的request会被重新调度下载。
                request.cookies = self._get_random_cookies()
                self.logger.debug('Using Cookies' + json.dumps(request.cookies))
                return request
            except Exception:
                raise IgnoreRequest
        #客户端发送的 HTTP 数据流包含一个过长网址， 即字节太多，被服务器414拒绝了，此时重新发送request
        elif response.status in [414]:
            return request
        else:
            return response
