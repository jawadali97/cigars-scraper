from typing import Iterable
import scrapy


class CigarpageSpider(scrapy.Spider):
    name = "cigarpage"
    allowed_domains = ["www.cigarpage.com"]
    start_urls = ["https://www.cigarpage.com"]

    def start_requests(self):
        yield scrapy.Request(url= 'https://www.cigarpage.com/brands', callback=self.parse)
    
    def parse(self, response):
        print(type(response))
