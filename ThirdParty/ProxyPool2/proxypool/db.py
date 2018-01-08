import redis
from ThirdParty.ProxyPool2.proxypool.error import PoolEmptyError
from ThirdParty.ProxyPool2.proxypool.setting import HOST, PORT, PASSWORD


class RedisClient(object):
    def __init__(self, host=HOST, port=PORT):
        if PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)


#从队列左侧拿出ip地址并删除已经被取出的ip地址
    def get(self, count=1):
        """
        get proxies from redis
        """
        #取出全部0~count范围内的ip
        proxies = self._db.lrange("proxies", 0, count - 1)
        #删除0~count范围的ip
        self._db.ltrim("proxies", count, -1)
        return proxies


#把有效的ip地址放到队列右侧
    def put(self, proxy):
        """
        add proxy to right top
        """
        self._db.rpush("proxies", proxy)


#移除并返回redis队列中最后一个IP地址
    def pop(self):
        """
        get proxy from right.
        """
        try:
            return self._db.rpop("proxies").decode('utf-8')
        except:
            raise PoolEmptyError

    @property
    def queue_len(self):
        """
        get length from queue.
        """
        return self._db.llen("proxies")

    def flush(self):
        """
        flush db
        """
        self._db.flushall()


if __name__ == '__main__':
    conn = RedisClient()
    print(conn.pop())
