import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from JDSpider.Config import *
import pymongo
import time


class JDSpider:

        def __init__(self):
            client = pymongo.MongoClient(MONGO_URL)
            self.db = client[MONGO_DB]
            # self.browser = webdriver.PhantomJS(service_args=SERVICE_ARGS,
            #                               executable_path='/Users/Chan/phantomjs-2.1.1-macosx/bin/phantomjs')

            #开启chrome headless模式
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3080.5 Safari/537.36')
            self.browser = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/Chan/chromeDriver/bin/chromedriver')
            self.wait = WebDriverWait(self.browser, 20)
            self.browser.set_window_size(1400, 900)

        def search(self):
            print('正在搜索')
            try:
                self.browser.get('https://www.jd.com')
                #搜索输入框
                searchInput = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#key'))
                )
                #确定搜索按钮
                submitBtn = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div.form > button')))
                searchInput.send_keys(KEYWORD)
                submitBtn.click()
                #点击搜索后，拿到商品页的总页数
                self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                totalPage = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1)')))
                self.get_products()
                return totalPage.text
            except TimeoutException:
                print('serch出错，正在重试')
                return self.search()


        def next_page(self,page_number):
            print('正在翻页', page_number)
            try:
                #等待输入页数的输入框加载出来
                input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input'))
                )
                #等待确定按钮加载完毕
                submit = self.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
                input.clear()
                input.send_keys(page_number)
                submit.click()
                #等待当前页码的按钮上面的页数加载出来（当前页码的按钮样式和其他按钮的样式不同）
                self.wait.until(EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page_number)))
                self.get_products()
            except TimeoutException:
                print('翻页出错，正在重试')
                self.next_page(page_number)


        def get_products(self):
            print('获取商品信息')
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li')))
            html = self.browser.page_source
            doc = pq(html)
            items = doc('#J_goodsList > ul > li').items()
            for item in items:
                product = {
                    'image': item.find('img').attr('src'),
                    'price': item.find('.p-price').text(),
                    'comment': item.find('.p-commit').text()[:-3],
                    'title': item.find('.p-name').text(),
                    'shop': item.find('.J_im_icon').text(),
                }
                self.save_to_mongo(product)


        def save_to_mongo(self,result):
            try:
                if self.db[MONGO_TABLE].insert(result):
                    print('存储到MONGODB成功', result)
            except Exception:
                print('存储到MONGODB失败', result)


        def getComputerInfo(self):
            # try:
            #     total = self.search()
            #     total = int(re.compile('(\d+)').search(total).group(1))
            #     for i in range(2, total+1):
            #         self.next_page(i)
            # except Exception:
            #     print('出错啦')
            # finally:
            #     self.browser.close()

            total = self.search()
            total = int(re.compile('(\d+)').search(total).group(1))
            for i in range(2, total + 1):
                self.next_page(i)

            self.browser.close()




