
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest
from Test.TestSpider.items import ZhihuItem


class ZhihuSipder(CrawlSpider) :
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/question/60347845"
    ]

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    }

    rules = [
        Rule(LinkExtractor(allow=[]),
                        callback='parse_page',
                        process_links='_xm_process_link',
                        process_request = '_xm_process_req',
                        follow=True
             )
    ]




    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://www.zhihu.com/",
                        # meta = {'cookiejar' : 1},
                        headers=self.headers,
                        callback = self.post_login)]

    #FormRequeset出问题了
    def post_login(self, response):
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print('*********xsrf:************',xsrf)
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
                            # meta = {'cookiejar' : response.meta['cookiejar']},
                            url='https://www.zhihu.com/login/email',
                            headers = self.headers,
                            formdata = {
                            '_xsrf': xsrf,
                                'email': 'xxxxxx',
                                'password': 'xxxxxx',
                            'captcha_type': 'cn'
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]


    def after_login(self, response) :
        for url in self.start_urls :
            yield Request(url)


    def parse_page(self, response):
        print('$$$$$$$$',response.url)
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        print(item)
        return item



    def _xm_process_link(self,links):
        for link in links:
            print('xxxxx', link.url)
            # 1
            if 'question' in link.url:
                continue  # skip all links that have "question" in their url
            # 2
            link.url = link.url + '/'  # fix url to avoid unnecessary redirection
            yield link


    def _xm_process_req(self, req):
        # 1
        req = req.replace(headers={'Cookie': 'foobar'})
        return req
        # 2
        if 'foo' in req.url:
            return req.replace(callback=self.parse_foo)
        elif 'bar' in req.url:
            return req.replace(callback=self.parse_bar)
        return req

