import scrapy


class JrcigarsSpider(scrapy.Spider):
    name = "jrcigars"
    allowed_domains = ["www.jrcigars.com"]
    start_urls = ["https://www.jrcigars.com"]

    def parse(self, response):
        pass
