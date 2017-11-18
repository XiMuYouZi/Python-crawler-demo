from .sql import SQL
from dingdian.dingdian.items import  *


class DingDianMongoDBPipeLine(object):
    def process_item(self,item,spider):
        sql = SQL()
        if isinstance(item,DingdianItem):
            sql.insert_novel_info(dict(item))

        if isinstance(item,novelChapterInfoItem):
            sql.insert_chapter_info(dict(item))


