from dingdian.dingdian.mySqlPipeLine.MongoHandler import *
from dingdian.dingdian.items import  *
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class DingDianMongoDBPipeLine(object):
    def process_item(self,item,spider):
        mongodb = MongoDB()
        if isinstance(item,novelInfoItem):
            mongodb.insert_novel_info(dict(item))

        if isinstance(item,novelChapterInfoItem):
            mongodb.insert_chapter_info(dict(item))



# class CustomImagesPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield scrapy.Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item