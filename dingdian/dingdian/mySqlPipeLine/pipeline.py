from .sql import SQL
from dingdian.dingdian.items import  DingdianItem


class DingDianMongoDBPipeLine(object):
    def process_item(self,item,spider):
     if isinstance(item,DingdianItem):
         sql = SQL()
         sql.insert_novel_info(item['nameID'],item['name'],item['author'],item['category'],item['url'],item['status'],item['cover'],item['collect_num'],item['content_len'],item['last_refresh_time'],item['desc'])