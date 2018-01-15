from Crawler.haixinSpider.parseHtml import *

par = parseHtml()
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    # 'X-UDID':'AMDig8AA_gyPTpqBEmYlS94XY3Dx47Dtc_A=',
    # 'Referer':'https://www.zhihu.com/people/excited-vczh/',
    # 'Host':'www.zhihu.com'
}

print(par.getStaticHtmlConten(
    url='http://www.zhihu.com/api/v4/members/zhangyueqian/followers?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics',
    headers=DEFAULT_REQUEST_HEADERS, cookies=''))
