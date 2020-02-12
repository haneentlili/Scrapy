# -*- coding: utf-8 -*-
import scrapy 
import scrapy.selector
from scrapy_spider.items import ScrapySpiderItem
import re
#from bs4 import BeautifulSoup

class QuotesSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?i=specialty-aps&srs=18505457011&qid=1581084452&ref=sr_pg_3']
    #start_urls = ['https://www.amazon.com//Oculus-Quest-Travel-Case-Compatible-Headsets/dp/B07Q1JH58V/ref=sr_1_65?qid=1581409367&sr=8-65&srs=18505457011']
    def parse(self, response):
        nextpage = response.xpath("//li[@class='a-last']/a/@href")
        for item in self.scrape(response):
            yield item 
        if nextpage:
            path = nextpage.extract_first()
            nextpage = response.urljoin(path)
            yield scrapy.Request(nextpage, callback=self.parse)
        
    def scrape(self, response):
        t = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").extract()
        r= response.xpath("//span[@class='a-icon-alt']/text()").extract()
        p= response.xpath("//span[@class='a-color-base']/text()").extract()
        im= response.xpath("//img/@src").extract()
        l = response.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a/@href").extract()
        #cin=response.xpath("//table[@class='a-keyvalue prodDetTable']//tr[1]/td[1]/text()").extract()
        #response.xpath("//span[@class='a-size-large']/text()").extract_first()
        datas=zip(t,r,p,im,l)
        for i in datas:
            item = ScrapySpiderItem()
            item['title']=i[0]
            item['rating']=i[1]
            item['price']=i[2]
            item['image']=i[3]
            res = "https://www.amazon.com/"+i[4]
            asin=re.findall(r"(?<=dp/)[A-Z0-9]{10}",res)[0]
            item['_id']=asin
            yield item
# =============================================================================
#         next_page = response.xpath("//li[@class='a-last']//a//@href").extract()
#         if next_page:
#             url = response.urljoin(next_page[0].extract())
#             yield scrapy.Request(url, self.parse)
# =============================================================================
