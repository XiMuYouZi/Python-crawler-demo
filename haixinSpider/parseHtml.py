#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import hashlib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart,MIMEBase
import smtplib
import json
import requests
from  pyquery import PyQuery as pq
from requests.exceptions import RequestException
from selenium import webdriver


class SendMail:

    def __init__(self):
        self.from_addr = '1214251739@qq.com'
        self.password = 'erkezuuzeesgiagb'  # qq授权码
        #349176813@qq.com
        haixin = '349176813@qq.com'
        ws2 = 'wangsheng9297@163.com'
        self.to_addr = [haixin,ws2]
        self.smtp_server = 'smtp.qq.com'
        self.msg = ''
        self.server = smtplib.SMTP_SSL()
        self.__configServer()

    def __format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    def __configServer(self):
        self.server = smtplib.SMTP_SSL(self.smtp_server, 465)  # 使用SSL加密传输
        # self.server.set_debuglevel(1)
        self.server.login(self.from_addr, self.password)


    def sendPlainEmail(self, text):
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = self.__format_addr('我是勤劳的小爬虫 <%s>' % self.from_addr)
        # s1 = ','.join(self.to_addr)

        msg['To'] = ','.join(self.to_addr)
        msg['Subject'] = Header('小主，您的新闻又更新啦', 'utf-8').encode()
        self.msg = msg
        self.__sendEamil()

    def sendAttachEmail(self,picPath):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.__format_addr('Python爱好者 <%s>' % self.from_addr)
        self.msg['To'] = self.__format_addr('管理员 <%s>' % self.to_addr)
        self.msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

        # 邮件正文是MIMEText:
        self.msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
        #添加图片附件
        with open(picPath, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename='test.png')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            self.msg.attach(mime)

        # 添加附件2，传送当前目录下的 1.txt 文件
        att1 = MIMEText(open('1.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        self.msg.attach(att1)
        self.__sendEamil()


    def __sendEamil(self):
        self.server.sendmail(self.from_addr, self.to_addr, self.msg.as_string())
        self.server.quit()



foshan = 'http://bendi.news.163.com/guangdong/special/04178D7C/foshanjbc.js'
dongguan = 'http://bendi.news.163.com/guangdong/special/04178D75/dongduanxinxiliu.js'
zhanjiang = 'http://bendi.news.163.com/guangdong/special/04178DAL/zhanjiangxinxiliu.js'
shantou = 'http://bendi.news.163.com/guangdong/special/04178D9D/xinxiliu.js'
chaozhou = 'http://bendi.news.163.com/guangdong/special/04178D6T/czxinxiliu.js'
jieyang = 'http://bendi.news.163.com/guangdong/special/04178D8D/jyxinxiliu.js'
zhuhai = 'http://bendi.news.163.com/guangdong/special/04178SVQ/web_index2016_centernews1.js'
huizhou = 'http://bendi.news.163.com/guangdong/special/04178KC4/hzxinxiliu.js'
shaoguan = 'http://bendi.news.163.com/guangdong/special/04178D9T/sgxinxiliu.js'
CSLJL = 'http://www.zsbtv.com.cn/a/spyp/dslm/cityzero/two_zerolist.shtml'
XQRX = 'http://www.fstv.com.cn/news/xqrx'
ZHYW = 'http://www.hizh.cn/localnews/index.jhtml'
MMXW = 'http://www.mm111.net/news/mmxw/'
#38：广州，39：深圳，85：珠海，87：汕头，韶关：90，惠州：76，东莞：41，湛江：75
SouthPlus = 'https://api.nfapp.southcn.com/nanfang_if/getArticles?columnId=14&lastFileId=0&count=20&rowNumber=0&version=0'
ChinaWeather = 'http://www.weather.com.cn/alarm/newalarmlist.shtml?areaId=10128'

#各大城市最后一次爬取的新闻内容
CSLJLLastparsedString =''
XQRXLastparsedString =''
ZHYWLastparsedString =''
MMXWLastparsedString = ''
SouthPlusLastparsedString =''
ChinaWeatherLastparsedString =''
WANGYINewsDic = {
    'foshan_KEY': '',
    'dongguan_KEY':'',
    'zhanjiang_KEY':'',
    'shantou_KEY':'',
    'chaozhou_KEY':'',
    'jieyang_KEY':'',
    'zhuhai_KEY':'',
    'shaoguan_KEY':'',
    'huizhou_KEY':''
}



SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
header = \
{
# 'Host': 'huaban.com',
# 'Connection': 'keep-alive',
# 'Pragma': 'no-cache',
# 'Cache-Control': 'no-cache',
# 'Upgrade-Insecure-Requests': 1,
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://huaban.com/search/?q=%E7%BE%8E%E5%A5%B3',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie': 'UM_distinctid=15b9a2117ad493-07663b9ea1e5d1-396a7807-13c680-15b9a2117ae37a; _uab_collina=150224242324971480915926; CNZZDATA1256914954=1307721638-1497797793-http%253A%252F%252Fwww.poluoluo.com%252F%7C1508119458; referer=https%3A%2F%2Fwww.google.com%2F; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAAFh0lEQVRYR8WXCWxUVRSGv9O9gGKAsLTsaI2iNAJv2JS%2BasSNBFRCgomyhcWiKOCGBBAIoBKgRWkwQXCJVhBwIdLI4kxZBGYKigIaLDQUBIRaIlZoafuOuTOvw5SytKbEm0zmzcxdznfOf%2F73RlBV3DF1%2FnzaFxUxYelSnKio4Lcq0g%2F4GmgrUFY9t67vCrOAGIFpdV1zpXmZJZnhOK%2F0u0SCjF%2B2jHbHjjFt7tzwXBW5C9gEtBOoqm8wCuOBlgKz67s2cn69QVIOHWLKwoVEV1VRFR1tKmMBnwB3AvcAg4HlQHPgceADgQKFGCAD8ABFwCqBfQqjgKXuHt2AlwS2BqsNA4GhwAlgr8BqhTbA%2B64KXgE%2BAuZklWRWXisRNSoyasUKlk6YwOJJk8Jrps6fbyBSgD6AA%2FwATBHY4spmJ%2FAtkAN8CqwHtgGvm4DdiqQITFboC%2BwAugA2cAfwKvAC0MLIT2GOgQX6A38Ah4HkrJJMc33VUQMkIzubFsXFzJ4xI1JaBiLPSMsF2QK84QY5ETgA%2BN3guws4CiOAmwWWaKhKyW6QAnhNhoHppqICZzWUqGxgANDY3auHe57pz9H1Ahm5cmWw2WfNnBkJ0hVYC5h303AB4DmBXQqRIIVAB4F%2FFN4Dfjd94YKYbJtrA2LWTybUM88L%2FKwwCHjTPcNIdCPwQATIM1klmSV1qkiXw4fJzsggvrycYTk5nGzTJnhdlpBgyv4W8JArC%2BMERuu5wBLAANzrZtn00Co3qFKgN5DmBn2%2FK8%2FRhCT2BPAhMBVY7AY5DLjo9lNPQi75vVsRI9nrS6tTYSGxFRXBJi%2BPj%2BdI584klJVxITExFThnNAz8BBhfftht6FNAExfGNGMv93AjNyMNk%2F0kINE1i7%2BArdXup6Eqm323u%2FMLjAyBC4Qc0rzijX1nlWQerBPI1VHFyOF%2FH%2FWy3ytGK7VB1LurLRK9CqUCIRYoENsarj7%2FepBmoQrISrF7vlO9p27Pb0%2BlY3qtERI1V9J6GoerMULrSUHJlXTPi5ffR0RhyJG72dmqiONNTHEvjRquVVcQM099%2FpEgy0F3i%2B0xmke93hikyQnQL8X2jA1DhL4%2FirAOlXXgfGN6R2yPkV5wqNe%2FGZGb0BZpSHER6Ltie8I30TVFK%2FWRohQaVcaxocOv%2FNb0z4YBcWF2gnQnNq6d9Es9rdv29KDK2USic5v06hU%2BSfMCE1AWoY2aS3rXUvX5%2FSDFYluPBvfJz29KqZ4BBolt5arPbwDGie1pVR1t4MAXej6mAutMW3xJRzh0S3EDgngDQxA%2BBxaJbU1RX%2BBjoLXY1oORp6gv8DbKRBo5yQZQfX7jRK3F9nQOJSQ%2FHXQzUQyV%2FtZazfPPwWEqcfFJJkFmjukRI61xB3vxXfLhhgUJBRE4CsSKbSWp138ckTEmqzVB%2FLkgXcW22l%2BqJM3E9twe%2FJznn4JjLN7pKOm9jwdBlNdI1NbVlTUg0U4UY36xbhBI8FAxT7YLUJ6UdOvWWk18WYbdijQPgxhJVlbtJoqnJM2zOgwSG58cWZEbC%2BItTIDiUwhNgXliW7Ue1zUoQc2pzrB6%2FT8C%2B4mLn0xlWWOclieRM2dRGSnp1mfq9WeCDDRJUd%2Be%2B8Tusa1aWmMPetjYroDCm2ve6P%2Bza9WQjjewBnRwpKZrVcUb2IVoNCLbcRhJXFwKFy9uQDTVAHJepiM8jcgMVBcgjEDF3N3NA%2BRjWd12bOh7qgM9TydzovHffNXxIBXRl%2F5VNAzItr2pOFXjJc169ooWXm2xvsAS0E7Exo8Oulxe%2FnBUk8W25rlNPxl1Bhhbl3Rrjfp290GihuKUvpyVuq%2Bi%2B5mk4MNeYlUs%2B5ud4lxcefi4BgG5VvAN9dsNubM3VHD12ed6IP8CjWOBN9vaFkcAAAAASUVORK5CYII%3D%2CMacIntel.1440.900.24; _hmt=1; sid=sKMcuZgCRGhfWdBa947gqyK4Yi3.hHwLId1%2FcZ3Tz32aPMIT1b5qjRY4jVyovJtqhgrpyjQ; _ga=GA1.2.1600592015.1492939511; _cnzz_CV1256903590=is-logon%7Clogged-out%7C1508635626809; CNZZDATA1256903590=598059047-1492936490-null%7C1508635467; __asc=ac5d195815f41af7aa9be806d90; __auc=902a4fc815b9a2115f366ca7a61'
}


class parseHtml:

    def  getStaticHtmlConten(self, url):

         try:
            r = requests.post(url, headers=header)
            if r.status_code == 200:
                r.encoding = r.apparent_encoding
                text = r.text
                return text
            return None
         except RequestException:
            return None



    def getCSLJLNews(self):
        global CSLJLLastparsedString
        htmlContent = self.getStaticHtmlConten(CSLJL)
        doc = pq(htmlContent)
        # .zsbtv-cont:first-child-----》父元素里面class=.zsbtv-cont的第一个标签
        # .zsbtv-cont :first-child-----》class = .zsbtv-cont元素的后代元素里面，每个元素的第一个标签
        # .zsbtv-cont>:first-child-----》父元素为.zsbtv-cont的子元素里面的第一个子元素，注意和上面的作对比，此处是直接的父子关系，上面是后代关系，不是直接的父子关系

        generator1 = list(doc('#left_list .zsbtv-cont:first-child .video_img a:first-child').items())
        generator2 = list(doc('#left_list .zsbtv-cont:first-child .video_img .video_time').items())

        list1 = []
        list2 = []
        list3 = []

        for item in generator2:
            string = item.text()+'\n'
            list1.append(string)

        for item in generator1:
            s =  'http://www.zsbtv.com.cn/' + item.attr('href')+'\n'
            list3.append(s)

        for item in generator1:
            s = item.attr('title') +'\n'
            list2.append(s)

        list4 = [str(str1) + str(str2) + str(str3) for str1, str2,str3 in zip(list1[:5], list2[:5], list3[:5])]
        parsedString = '分类：城市零距离'+'\n \n'
        parsedString += ' \n'.join(list4)
        parsedString += '\n \n ===================================================================================================================================== \n \n'
        if CSLJLLastparsedString != '':
            if self.md5(CSLJLLastparsedString) == self.md5(parsedString):
                return ''
            else:
                CSLJLLastparsedString = parsedString
                return parsedString
        else:
            CSLJLLastparsedString = parsedString
            return parsedString



    def getXQRXNews(self):
        global XQRXLastparsedString
        htmlContent = self.getStaticHtmlConten(XQRX)
        doc = pq(htmlContent)

        generator1 = list(doc('#content div:nth-child(2) ul li ').items())

        for item in generator1:
            news = {
                'title':item.find('h2 a').attr('title'),
                'href': item.find('h2 a').attr('href'),
                'time': item.find('.date').text()

            }

            print(news)

            # for item in generator2:
        #     l1.append(item.text()+'\n')
        #
        # for item1 in generator1:
        #     string = item1.attr('href') + '\n'
        #     l3.append(string)
        #
        # for item in generator1:
        #     string =  item.attr('title') +'\n'
        #     l2.append(string)
        #
        #
        # l4 = [str(str1) + str(str2) + str(str3) for str1, str2,str3 in zip(l1[:5], l2[:5], l3[:5])]
        # parsedString = '分类：小强热线' + '\n \n'
        # parsedString += ' \n'.join(l4)
        # parsedString += '\n \n ===================================================================================================================================== \n \n'
        # if XQRXLastparsedString != '':
        #     if self.md5(XQRXLastparsedString) == self.md5(parsedString):
        #         return ''
        #     else:
        #         XQRXLastparsedString = parsedString;
        #         return parsedString
        # else:
        #     XQRXLastparsedString = parsedString;
        #     return parsedString;



    def getZHYWNews(self):
        global ZHYWLastparsedString
        htmlContent = self.getStaticHtmlConten(ZHYW)
        doc = pq(htmlContent)

        generator1 = list(doc('#newsList  .t_news .txt_t .news_tit02 p a').items())
        generator2 = list(doc('#newsList  .t_news .txt_t .news_info span').items())

        l1 = []
        l2 = []
        l3 = []

        for item in generator2:
            l1.append(item.text()+'\n')

        for item in generator1:
            string =  item.text() + '\n'
            l2.append(string)

        for item in generator1:
            string =  item.attr('href')+'\n'
            l3.append(string)

        l4 = [str(str1) + str(str2) + str(str3) for str1, str2, str3 in zip(l1[:5], l2[:5], l3[:5])]
        parsedString = '分类：珠海新闻网·珠海要闻' + '\n \n'
        parsedString += ' \n'.join(l4)
        parsedString += '\n \n ===================================================================================================================================== \n \n'
        if ZHYWLastparsedString != '':
            if self.md5(ZHYWLastparsedString) == self.md5(parsedString):
                return ''
            else:
                ZHYWLastparsedString = parsedString
                return parsedString
        else:
            ZHYWLastparsedString = parsedString
            return parsedString



    def getMMXWNews(self):
        global MMXWLastparsedString
        htmlContent = self.getStaticHtmlConten(MMXW)
        doc = pq(htmlContent)
        generator1 = list(doc('#list  ul li h3 a ').items())
        generator2 = list(doc('#list ul li .m-imagetext div a span').items())

        l1 = []
        l2 = []
        l3 = []

        for item in generator2:
            l1.append( item.text()+'\n')


        for item in generator1:
            string =  item.text() + '\n'
            l2.append(string)

        for item in generator1:
            string =  item.attr('href')+'\n'
            l3.append(string)


        l4 = [str(str1) + str(str2) + str(str3) for str1, str2, str3 in zip(l1[:5], l2[:5], l3[:5])]
        parsedString = '分类：茂名新闻网' + '\n \n'
        parsedString += ' \n'.join(l4)
        parsedString += '\n \n ===================================================================================================================================== \n \n'
        if MMXWLastparsedString != '':
            if self.md5(MMXWLastparsedString) == self.md5(parsedString):
                return ''
            else:
                MMXWLastparsedString = parsedString
                return parsedString
        else:
            MMXWLastparsedString = parsedString
            return parsedString



    def getWangYiNews(self,url):
        jsonStr = self.getStaticHtmlConten(url)
        jsonStr = re.sub('data_callback\(', '', jsonStr)
        jsonStr = re.sub('\)', '', jsonStr)

        datas = json.loads(jsonStr, strict=False)
        l1 = []
        if datas:
            for data in datas:
                string= data.get('time')+'\n' + data.get('title') +'\n' +data.get('docurl')+'\n'
                l1.append(string)
        l1 = l1[:5]
        return  self.HandleWangYiNewsUpdate(l1,url)



    def HandleWangYiNewsUpdate(self, news, url):
        global WANGYINewsDic, key
        if url == foshan:
            category = '网易佛山'
            key = 'foshan_KEY'
        if url == dongguan:
            category = '网易东莞'
            key = 'dongguan_KEY'
        if url == zhanjiang:
            category = '网易湛江'
            key = 'zhanjiang_KEY'
        if url == shantou:
            category = '网易汕头'
            key = 'shantou_KEY'
        if url == chaozhou:
            category = '网易潮州'
            key = 'chaozhou_KEY'
        if url == jieyang:
            category = '网易揭阳'
            key = 'jieyang_KEY'
        if url == zhuhai:
            category = '网易珠海'
            key = 'zhuhai_KEY'
        if url == huizhou:
            category = '网易惠州'
            key = 'huizhou_KEY'
        if url == shaoguan:
            category = '网易韶关'
            key = 'shaoguan_KEY'

        parsedString = '分类：%s' % category + '\n \n'
        parsedString += ' \n'.join(news)
        parsedString += '\n \n ===================================================================================================================================== \n \n'
        LastparsedString = WANGYINewsDic.get(key)
        if LastparsedString != '':
            if self.md5(LastparsedString) == self.md5(parsedString):
                return ''
            else:
                WANGYINewsDic[key] = parsedString
                return parsedString
        else:
            WANGYINewsDic[key] = parsedString
            return parsedString


    def getSouthPlusNews(self):
        global SouthPlusLastparsedString
        jsonStr = self.getStaticHtmlConten(SouthPlus)

        datas = json.loads(jsonStr, strict=False)
        l1 = []
        if datas:
            for data in datas:
                string = data.get('publishtime') + '\n' + data.get('title') + '\n' + data.get('shareUrl') + '\n'
                l1.append(string)
        l1 = l1[:10]

        parsedString = '分类：南方Plus' + '\n \n'
        parsedString += ' \n'.join(l1)
        parsedString += '\n \n ===================================================================================================================================== \n \n'
        if SouthPlusLastparsedString != '':
            if self.md5(SouthPlusLastparsedString) == self.md5(parsedString):
                return ''
            else:
                SouthPlusLastparsedString = parsedString
                return parsedString
        else:
            SouthPlusLastparsedString = parsedString
            return parsedString



    def getChinaWeatherNews(self):
        global  ChinaWeatherLastparsedString
        browser = webdriver.PhantomJS(service_args=SERVICE_ARGS,executable_path = '/Users/Chan/phantomjs-2.1.1-macosx/bin/phantomjs')
        browser.set_window_size(1400, 900)
        browser.get(ChinaWeather)
        htmlContent = browser.page_source

        doc = pq(htmlContent)
        generator1 = list(doc('.dDUl li a:nth-of-type(2)').items())
        generator2 = list(doc('.dDUl li span:nth-of-type(2)').items())

        l1 = []
        l2 = []

        for item1 in generator1:
            string = item1.text() + '\n' + item1.attr('href') +'\n'
            l2.append(string)

        for item2 in generator2:
            string = item2.text()+'\n'
            l1.append(string)

        l4 = [str(str1) + str(str2)  for str1, str2 in zip(l1[:10], l2[:10])]
        parsedString = '分类：中国天气网' + '\n \n'
        parsedString += ' \n'.join(l4)
        parsedString += '\n \n ===================================================================================================================================== \n \n'
        if ChinaWeatherLastparsedString != '':
            if self.md5(ChinaWeatherLastparsedString) == self.md5(parsedString):
                return ''
            else:
                ChinaWeatherLastparsedString = parsedString
                return parsedString
        else:
            ChinaWeatherLastparsedString = parsedString
            return parsedString


    def sendAllNewsToEmail(self):
        news = self.getMMXWNews()+self.getZHYWNews()+self.getCSLJLNews()+self.getXQRXNews()+self.getSouthPlusNews()+self.getChinaWeatherNews()
        city_list = [foshan,dongguan,zhanjiang,shantou,chaozhou,jieyang,zhuhai,huizhou,shaoguan]
        for city in city_list:
            news += self.getWangYiNews(city)
        if news != '':
            sender = SendMail()
            sender.sendPlainEmail(news)
        return  news


    def md5(self,text):
        m = hashlib.md5()
        m.update(text.encode('utf-8'))
        md5Str = m.hexdigest()
        return md5Str
