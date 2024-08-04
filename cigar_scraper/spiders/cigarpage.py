from typing import Iterable
import scrapy
from cigar_scraper.items import CigarScraperItem, CigarPack



class CigarpageSpider(scrapy.Spider):
    name = "cigarpage"
    allowed_domains = ["www.cigarpage.com"]
    start_urls = ["https://www.cigarpage.com"]
    use_selenium =  True
    set_timeout = 20

    def start_requests(self):
        yield scrapy.Request(url= 'https://www.cigarpage.com/brands', callback=self.parse)
    
    def parse(self, response):
        container = response.css('section .std .row')
        # brands = container.css('h4 span ::text').getall()
        # # links = container.css('.brand-item >a')
        # cigars = container.css('.brand-item >a ::text').getall()
        # cigar_links = container.css('.brand-item >a ::attr(href)').getall()

        # # print('Brand: ', brands)
        # # print('Cigar: ', cigars)
        # # print('URL: ', cigar_links)


        brand_list = []
        
        # Find all h4 brand summaries and all divs with brand-item
        brands = response.css('h4.brand-summary')
        items = response.css('div.brand-item')
        
        current_brand = None
        brand_name = ''
        for element in response.css('div.row > div.col-xs-12.col-sm-4 > *'):
            if 'brand-summary' in element.attrib.get('class', ''):
                # This is an h4 element with class brand-summary
                if current_brand:
                    # Append the previous brand's data to the brand list
                    brand_list.append(current_brand)
                    
                # Start a new current_brand dictionary
                brand_name = element.css('span::text').get().strip()
                current_brand = {'brand_name': brand_name, 'urls': []}
            elif 'brand-item' in element.attrib.get('class', ''):
                # This is a div element with class brand-item
                if current_brand:
                    link = element.css('a::attr(href)').get()
                    yield response.follow(link, self.parse_cigar_page, cb_kwargs={'brand': brand_name})

                    # current_brand['urls'].append(link)
        
        if current_brand:
            # Append the last brand's data to the brand list
            brand_list.append(current_brand)
        
        # yield {'brands': brand_list}


        # for brand in brand_list:
        #     for link in brand['urls']:
        #         # link = "https://www.cigarpage.com/601-blue-label-maduro.html"
        #         # link = "https://www.cigarpage.com/brands"
        #         yield response.follow(link, self.parse_cigar_page, cb_kwargs={'brand': brand['brand_name']})

    
    
    def parse_cigar_page(self, response, brand):


        name = response.css('h1.productHeader ::text').get()

        #grouped-items-container > div > div > table

        #grouped-items-container > div > div > table > tbody > tr:nth-child(2)


        table = response.css('div#grouped-items-container div > div > table.cigar-grid')

        rows = table.css('tbody tr')

        print('Rows::: ', len(rows))
        print('Brand Name::: ', brand)
        print('Cigar name::: ', name)
        print('***************************************\n')



        # f = open("test.html", "a")
        # f.write(str(response.text))
        # f.close()


        




        # product = CigarScraperItem()
        
        # # Get prices for all packs
        # packs_list = []
        # table = response.css('#product_table >tr')
        # for row in table[1:]:
        #     pack = CigarPack()
        #     pack['name'] = row.css('td.lbup:not(.av_details) ::text').get()
        #     pack['availability'] = row.css('td div.lbup ::text').get()
        #     pack['price'] = row.css('td.important_price ::text').get()
        #     packs_list.append(dict(pack))

        # product['name'] = response.css('.product_primary_info h1 span::text').get()
        # product['packs'] = packs_list
        # product['prod_url'] = response.url

        # # Desired fields to extract, the key text is as per on the website
        # fields = {
        #     "Brands": "brand",
        #     "Cigar Shape": "shape",
        #     "Strength": "strength",
        #     "Cigar Ring Gauge": "ring",
        #     "Cigar Length": "length",
        #     "Origin": "origin",
        # }

        # for field in fields:
        #     # XPath to match <li> elements that have the desired fields as titles
        #     value = response.xpath(
        #         f"//div[@id='pr_tabSpec']//li/div[contains(text(),'{field}')]/following-sibling::div//meta/@content | "
        #         f"//div[@id='pr_tabSpec']//li/div[contains(text(),'{field}')]/following-sibling::div//div[contains(@class,'onHover')]/text()"
        #     ).get(default='').strip()

        #     if not value:  # Try an alternative approach if the text extraction fails
        #         value = response.xpath(
        #             f"//div[@id='pr_tabSpec']//li/div[contains(text(),'{field}')]/following-sibling::div/div[contains(text(),'{field}')]"
        #         ).xpath('following-sibling::div//meta/@content | following-sibling::div//div[contains(@class,"onHover")]/text()').get(default='').strip()

        #     if field == "Strength":
        #         value = response.xpath("//div[@id='strengthCursor']//div[not(@id)]/text()").get(default='').strip()
            
        #     # Assign the extracted value to the results dictionary
        #     product[fields[field]] = value
        
        # yield product




