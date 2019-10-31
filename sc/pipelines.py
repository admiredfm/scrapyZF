# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScPipeline(object):

    def open_spider(self,spider):
        print("开始了.......................")
        self.fn = open("wenjian.txt",'w',encoding='utf-8')

    def process_item(self, item, spider):

        self.fn.write(str(item))

        return item

    def close_spider(self,spider):
        self.fn.close()