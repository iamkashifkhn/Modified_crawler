# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline

class GitcrawlerPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        # print("this is my item", jsonData['title'])
        file_name: str = request.url.split("/")[-5]
        file_name2: str = request.url.split("/")[-6]
        file_name = f'{file_name2}_{file_name}-main.zip'
        return file_name