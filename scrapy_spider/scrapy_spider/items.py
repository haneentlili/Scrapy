import scrapy
class ScrapySpiderItem(scrapy.Item):
    _id = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()

    
    
