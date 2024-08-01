# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CigarScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NeptuneCigarItem(scrapy.Item):
    name = scrapy.Field()
    prod_link = scrapy.Field()
    bundles = scrapy.Field()

class NeptuneCigarBundle(scrapy.Item):
    pack = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()