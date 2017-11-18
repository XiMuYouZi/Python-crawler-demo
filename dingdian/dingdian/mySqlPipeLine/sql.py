import pymongo
from dingdian.dingdian import settings
from dingdian.dingdian.items import *

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_PASSWORD = settings.MYSQL_PASSWORD

DB_HOST = settings.MONGO_URL
DB_NAME = settings.MONGO_DB
DB_NOVEL_TABLE = settings.MONGO_NOVEL_TABLE
DB_CHAPTER_TABLE = settings.MONGO_CHAPTER_TABLE


class SQL:

      def __init__(self):
        client = pymongo.MongoClient(DB_HOST)
        self.db = client[DB_NAME]


      def insert_novel_info(self,item):
          try:
            if self.db[DB_NOVEL_TABLE].insert(item):
               print('存储小说信息成功')
          except Exception:
               print('存储小说信息失败')


      def insert_chapter_info(self, item):
          try:
              if self.db[DB_CHAPTER_TABLE].insert(item):
                  print('存储章节信息成功')
          except Exception:
              print('存储章节信息失败')