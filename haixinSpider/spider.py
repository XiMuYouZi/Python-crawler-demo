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
    news = parser.getChinaWeatherNews()
    print(news)


test()





