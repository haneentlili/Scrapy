# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #extracting data
        quotes = response.xpath("//span[@class='text']/text()").extract()
        the_author = response.xpath("//small[@class='author']/text()").extract()
        #packing data to couples
        row_data=zip(quotes,the_author)
        #returning data 
        for item in row_data:
            #creating dictionary tostore data
            dic_data={
                    'quote': item[0],
                    'its_author': item[1]
                    }
            #returning the data
            yield dic_data
            