# -*- coding: utf-8 -*-

# Scrapy settings for dingdian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dingdian'

SPIDER_MODULES = ['dingdian.dingdian.spiders']
NEWSPIDER_MODULE = 'dingdian.dingdian.spiders'

#cookie设置
COOKIES_DEBUG = True
COOKIES_ENABLED  = False

#自动限速，根据Scrapy服务器及您爬取的网站的负载自动限制爬取速度
AUTOTHROTTLE_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dingdian (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 3
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
REDIRECT_ENABLED = False
REACTOR_THREADPOOL_MAXSIZE = 10
#如果启用，当从相同的网站获取数据时，Scrapy将会等待一个随机的值 (0.5到1.5之间的一个随机值 * DOWNLOAD_DELAY)
RANDOMIZE_DOWNLOAD_DELAY = True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dingdian.middlewares.DingdianSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dingdian.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'dingdian.dingdian.mySqlPipeLine.pipeline.DingDianMongoDBPipeLine': 300,
   # 'dingdian.dingdian.mySqlPipeLine.pipeline.ImagesPipeline': 100,
   'dingdian.dingdian.mySqlPipeLine.pipeline.FilesPipeline': 20
}
FILES_STORE = '/Users/Chan/Downloads/downFiles'
IMAGES_STORE = '/Users/Chan/Downloads/downImages'
# 图像管道避免下载最近已经下载的图片。使用 FILES_EXPIRES (或 IMAGES_EXPIRES) 设置可以调整失效期限，可以用天数来指定:
FILES_EXPIRES = 90
IMAGES_EXPIRES = 30
#缩略图尺寸
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
#小于这个宽高的图片都丢弃不下载
IMAGES_MIN_HEIGHT = 50
IMAGES_MIN_WIDTH = 50

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PORT = '3306'
MYSQL_DB = 'dingdian'
MYSQL_PASSWORD = ''

MONGO_URL = 'localhost'
MONGO_DB = 'DINGDIAN'
MONGO_NOVEL_TABLE = 'novel_info'
MONGO_CHAPTER_TABLE = 'chapter_info'