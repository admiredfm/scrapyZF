# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #标题
    index_number = scrapy.Field()   #索引号
    sort = scrapy.Field()   #分类
    issuing_authority = scrapy.Field()  #发文机关
    written_date = scrapy.Field()   #成文日期
    release_date = scrapy.Field()   #发布日期
    send_text_number = scrapy.Field()   #发文字号
    content = scrapy.Field()    #内容

