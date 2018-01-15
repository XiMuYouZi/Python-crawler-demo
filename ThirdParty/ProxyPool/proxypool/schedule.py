import time
from multiprocessing import Process
import asyncio
import aiohttp
try:
    from aiohttp.errors import ProxyConnectionError,ServerDisconnectedError,ClientResponseError,ClientConnectorError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError,ServerDisconnectedError,ClientResponseError,ClientConnectorError
from ThirdParty.ProxyPool.proxypool.db import RedisClient
from ThirdParty.ProxyPool.proxypool.error import ResourceDepletionError
from ThirdParty.ProxyPool.proxypool.getter import FreeProxyGetter
from ThirdParty.ProxyPool.proxypool.setting import *
from asyncio import TimeoutError


# 检查ip地址是否有效，有效就放入redis，无效就不放入redis
class ValidityTester(object):
    test_api = TEST_API

    def __init__(self):
        self._raw_proxies = None
        self._usable_proxies = []

    def set_raw_proxies(self, proxies):
        self._raw_proxies = proxies
        self._conn = RedisClient()

    async def test_single_proxy(self, proxy):
        """
        text one proxy, if valid, put them to usable_proxies.
        """
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    if isinstance(proxy, bytes):
                        proxy = proxy.decode('utf-8')
                    real_proxy = 'http://' + proxy
                    print('Testing', proxy)
                    async with session.get(self.test_api, proxy=real_proxy, timeout=get_proxy_timeout) as response:
                        if response.status == 200:
                            self._conn.put(proxy)  #有效的ip放入队列
                            print('Valid proxy', proxy)
                except (ProxyConnectionError, TimeoutError, ValueError):
                    print('Invalid proxy', proxy)  #无效的ip不放入队列
        except (ServerDisconnectedError, ClientResponseError,ClientConnectorError) as s:
            print(s)
            pass

    def test(self):
        """
        aio test all proxies.
        """
        print('ValidityTester is working')
        try:
            loop = asyncio.get_event_loop()
            tasks = [self.test_single_proxy(proxy) for proxy in self._raw_proxies]
            loop.run_until_complete(asyncio.wait(tasks))
        except ValueError:
            print('Async Error')


#去各大免费ip代理网站爬取ip地址
class PoolAdder(object):
    """
    add proxy to pool
    """

    def __init__(self, threshold):
        self._threshold = threshold
        self._conn = RedisClient()
        self._tester = ValidityTester()
        self._crawler = FreeProxyGetter()

    def is_over_threshold(self):
        """
        judge if count is overflow.
        """
        if self._conn.queue_len >= self._threshold:
            return True
        else:
            return False

        #爬取ip地址
    def add_to_queue(self):
        print('PoolAdder is working')
        proxy_count = 0
        while not self.is_over_threshold():
            # 从FreeProxyGetter类的__CrawlFun__属性里面取出爬虫函数名字
            for callback_label in self._crawler.__CrawlFunc__:
                # 执行爬虫函数，得到爬取到的代理ip地址
                raw_proxies = self._crawler.get_raw_proxies(callback_label)
                # 测试每个ip地址，有效才加入redis
                self._tester.set_raw_proxies(raw_proxies)
                self._tester.test()
                #检测获取到的ip地址数量，达到最大数量就停止获取
                proxy_count += len(raw_proxies)
                if self.is_over_threshold():
                    print('IP is enough, waiting to be used')
                    break
            if proxy_count == 0:
                raise ResourceDepletionError


#定时任务，
class Schedule(object):
    @staticmethod
    #检查redis池里面的ip地址，无效就剔除然后重新获取，有效就不做操作
    def valid_proxy(cycle=VALID_CHECK_CYCLE):
        """
        Get half of proxies which in redis
        """
        conn = RedisClient()
        tester = ValidityTester()
        while True:
            print('Refreshing ip')
            #取出一半IP地址
            count = int(0.5 * conn.queue_len)
            if count == 0:
                print('Waiting for adding')
                time.sleep(cycle)
                continue
            raw_proxies = conn.get(count)
            tester.set_raw_proxies(raw_proxies)
            tester.test()
            time.sleep(cycle)

    @staticmethod
    #检查redis队列的ip地址数量是否足够，不够就去获取新的ip，足够就不做任何操作
    def check_pool(lower_threshold=POOL_LOWER_THRESHOLD,
                   upper_threshold=POOL_UPPER_THRESHOLD,
                   cycle=POOL_LEN_CHECK_CYCLE):
        """
        If the number of proxies less than lower_threshold, add proxy
        """
        conn = RedisClient()
        adder = PoolAdder(upper_threshold)
        while True:
            if conn.queue_len < lower_threshold:
                adder.add_to_queue()
            time.sleep(cycle)

    def run(self):
        print('Ip processing running')
        # 开启两条线程：
        # 1、执行从redis队列中取出ip进行有效性检查，
        # 2、爬取免费代理ip放入redis
        valid_process = Process(target=Schedule.valid_proxy)
        check_process = Process(target=Schedule.check_pool)
        valid_process.start()
        check_process.start()