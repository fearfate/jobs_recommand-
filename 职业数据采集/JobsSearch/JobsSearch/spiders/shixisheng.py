import scrapy


class ShixishengSpider(scrapy.Spider):
    name = 'shixisheng'
    allowed_domains = ['shixiseng.com']
    start_urls = ['https://www.shixiseng.com/',]


    def parse(self, response):

        pass
