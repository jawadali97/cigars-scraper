import scrapy
from cigar_scraper.items import NeptuneCigarBundle, NeptuneCigarItem


class NeptuneCigarSpider(scrapy.Spider):
    name = "neptune_cigar"
    allowed_domains = ["www.neptunecigar.com"]
    start_urls = ["https://www.neptunecigar.com"]


    def start_requests(self):
        # headers = {
        #     "Host": "www.cigarpage.com",
        #     "Connection": "keep-alive",
        #     "Cache-Control": "max-age=0",
        #     "Upgrade-Insecure-Requests": "1",
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        #     "DNT": "1",
        #     "Accept-Encoding": "gzip, deflate, sdch",
        #     "Accept-Language":"en-US,en;q=0.8"
        # }

        yield scrapy.Request(url= 'https://www.neptunecigar.com/cigars?pg=1&nb=48&sort=BeS', callback=self.parse)

    
    def parse(self, response):
        for product in response.css('div.product_item'):
            bundles_list = []

            # Get prices for all bundles
            table = product.css('table.product_table tr')
            for row in table[1:]:
                bundle = NeptuneCigarBundle()
                bundle['pack'] = row.css('td.lbup:not(.av_details) ::text').get()
                bundle['availability'] = row.css('td div.lbup ::text').get()
                bundle['price'] = row.css('td.important_price.ca_current_price span ::text').get()
                bundles_list.append(dict(bundle))

            item_object = NeptuneCigarItem()
            item_object['name'] = product.css('a.product_name >h2 ::text').get()
            item_object['prod_link'] = self.start_urls[0] + product.css('a.product_name ::attr(href)').get()
            item_object['bundles'] = bundles_list

            yield item_object

            # yield {
            #     'title': product.css('a.product_name >h2 ::text').get(),
            #     'product_link': self.start_urls[0] + product.css('a.product_name ::attr(href)').get(),
            #     'bundles': [
            #         {
            #             'pack': row.css('td.lbup:not(.av_details) ::text').get(),
            #             'availability': row.css('td div.lbup ::text').get(),
            #             'price': row.css('td.important_price.ca_current_price span ::text').get()
            #         } for row in table[1:]
            #     ],
            #     # 'bundles': [
            #     #     {
            #     #         'pack': table[1].css('td.lbup:not(.av_details) ::text').get(),
            #     #         'price': table[1].css('td.important_price.ca_current_price span ::text').get()
            #     #     },
            #     #     {
            #     #         'pack': table[2].css('td.lbup:not(.av_details) ::text').get(),
            #     #         'price': table[2].css('td.important_price.ca_current_price span ::text').get()
            #     #     }
            #     # ]
            #     # 'bundles': bundles_list
            # }
        
        list_items = response.css('div#pagination1 li')
        next_page = list_items[-1].css('a.pagination_buttons ::attr(href)').get()
        if next_page is not None:
            next_url = self.start_urls[0] + next_page
            yield response.follow(next_url, callback=self.parse)

            

        
        
