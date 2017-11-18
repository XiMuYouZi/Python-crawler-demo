import pymongo
from dingdian.dingdian import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_PASSWORD = settings.MYSQL_PASSWORD

DB_HOST = settings.MONGO_URL
DB_NAME = settings.MONGO_DB
DB_TABLE = settings.MONGO_TABLE

class SQL:

  def __init__(self):
    client = pymongo.MongoClient(DB_HOST)
    self.db = client[DB_NAME]

  def insert_novel_info(self,nameID,name,author,category,url,status,cover,collect_num,content_len,last_refresh_time,desc):
      novel_info = {
        'nameID':nameID,
        'name' : name,
        'url' : url,
        'cover' : cover,
        'author' : author,
        'collect_num' : collect_num,
        'content_len' : content_len,
        'last_refresh_time' : last_refresh_time,
        'desc' : desc,
        'category' : category,
        'status' : status
      }
      try:
        if self.db[DB_TABLE].insert(novel_info):
           print('存储到MONGODB成功')
      except Exception:
           print('存储到MONGODB失败')


