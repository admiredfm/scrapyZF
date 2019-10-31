# -*- coding: utf-8 -*-
import scrapy
from sc.items import ScItem


class ZcSpider(scrapy.Spider):
    name = 'zc'
    allowed_domains = ['sousuo.gov.cn','www.gov.cn']
    start_urls = ['http://sousuo.gov.cn/column/30469/0.htm']

    def parse(self, response):
        #获取当前页所有政策链接
        zclist = response.xpath("//*[@class='listTxt']/li")

        #获取每条政策详情
        for val in zclist:
            url = val.xpath("./h4/a/@href").extract()[0]
            yield scrapy.Request(url,callback=self.requstUrl)

        #找到下一页链接
        next_url = response.xpath("//div[@class='newspage cl']/ul/li[last()]/a[@class='next']/@href").get()
        
        #爬取下一页
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url,callback=self.parse)
            
    #获取详情
    def requstUrl(self,response):

        item = ScItem()

        head = response.xpath("//*[@class='bd1'][1]/tbody")
        item['index_number'] = head.xpath("./tr[1]/td[2]/text()").get()
        item['sort'] = head.xpath("./tr[1]/td[4]/text()").get()
        item['issuing_authority'] = head.xpath("./tr[2]/td[2]/text()").get()
        item['written_date'] = head.xpath("./tr[2]/td[4]/text()").get()
        item['title'] = head.xpath("./tr[3]/td[2]/text()").get()
        item['send_text_number'] = head.xpath("./tr[4]/td[2]/text()").get()
        item['release_date'] = head.xpath("./tr[4]/td[4]/text()").get()

        item['content'] = response.xpath("//*[@id='UCAP-CONTENT']").xpath('string()').get()
       
        return item