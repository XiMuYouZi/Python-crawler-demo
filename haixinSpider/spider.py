#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  haixinSpider.parseHtml import  *
import time

from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print('发送爬虫存活检测邮件')
    sender =  SendMail()
    sender.to_addr = ['wangsheng9297@163.com']
    sender.sendPlainEmail('如果你在每天11点收到这封邮件，说明勤劳的小爬虫还活着，如果收不到，那小爬虫已经累死了，请电联：18565489297')


def detecationSpider():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'cron', day_of_week='1-7', hour=11, minute=00)
    scheduler.start()


def spider():
    print('+++++++++++++++++++++++++++++++++++++')
    print('首次运行爬虫，开始爬取新闻')
    parser = parseHtml()
    news = parser.sendAllNewsToEmail()
    print('本次爬取时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('本次爬取内容：\n', )
    print(news)
    print('+++++++++++++++++++++++++++++++++++++')

    count = 0
    while True:
        time.sleep(900)
        count += 1
        print('第（%d）次循环运行爬虫，爬取新闻' % count)
        parser = parseHtml()
        news = parser.sendAllNewsToEmail()
        print('本次爬取时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print('本次爬取内容：\n', )
        print(news)
        print('+++++++++++++++++++++++++++++++++++++')



def main():
    detecationSpider()
    spider()


def test():
    parser = parseHtml()
    news = parser.getStaticHtmlConten('http://r.inews.qq.com/getSubNewsIndex?chlid=kQNSubscribeChannelMenuTypeArticle&startarticleid=&store=1&__qnr=1f468c0cd8d2&isJailbreak=0&omgid=bf7966cad0abac44e3c9e9dbdc32192ee890001011270f&idfa=00000000-0000-0000-0000-000000000000&idft=3E40D3B1-EED7-451B-8214-C6D3A6AF885B&appver=10.3.2_qqnews_5.3.9&network_type=wifi&omgbizid=c5ecb82836b71b4f534bcfdf3b70177be868006011270f&screen_height=667&devid=F2BA7649-C5E0-467F-B31E-23D9AE8EAB7B&screen_scale=2&idfv=F2BA7649-C5E0-467F-B31E-23D9AE8EAB7B&screen_width=375&device_model=iPhone&activefrom=icon&apptype=ios&startarticleid=&__qnr=1f468c0cb044&global_info=0%7C&omgid=bf7966cad0abac44e3c9e9dbdc32192ee890001011270f&idfa=00000000-0000-0000-0000-000000000000&qqnews_refpage=QNMineViewController&isJailbreak=0&appver=10.3.2_qqnews_5.3.9&network_type=wifi&device_model=iPhone8%2C1&omgbizid=c5ecb82836b71b4f534bcfdf3b70177be868006011270f&screen_height=667&devid=F2BA7649-C5E0-467F-B31E-23D9AE8EAB7B&screen_scale=2&screen_width=375&store=1&activefrom=icon')
    print(news)

if __name__ == '__main__':
    test()





