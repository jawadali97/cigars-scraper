import scrapy


class BestcigarPricesSpider(scrapy.Spider):
    name = "bestcigar_prices"
    allowed_domains = ["www.bestcigarprices.com"]
    start_urls = ["https://www.bestcigarprices.com"]
    use_selenium =  True
    set_timeout = 10

    def start_requests(self):

        # headers = {
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        #     "Accept-Encoding": "gzip, deflate, br, zstd",
        #     "Accept-Language": "en-PK,en-US;q=0.9,en;q=0.8",
        #     "Cache-Control": "max-age=0",
        #     "Cookie": "_ga=GA1.1.1809110159.1722010150; ssUserId=50642a66-0fbb-47eb-a42b-974f68e7cad6; _isuid=50642a66-0fbb-47eb-a42b-974f68e7cad6; ssSessionIdNamespace=dc019b76-606d-491c-ab19-9f52798246b8; cookie_cart_login=0; _vwo_uuid_v2=D0EECCBE7E4AB10C786438C388DE15A15|58eb858369b31d82ac1a983b4d658cbc; cf_clearance=u9SHexuA8XmBCcdiB9Dp4J3rHVdSaC_ofFgS1K_YfE0-1722010151-1.0.1.1-1yTePDu5SJLxiZrJLrv3o3rgBgDz3sDyWPBNXEksUf7mvhENU8qcGkDHhvgF35HfNk8KIhZ_ghHsMtpqbsTe1g; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; ltkSubscriber-Account=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; _wingify_pc_uuid=09b54e34f0e6420c86d0b83712f6408f; _gcl_au=1.1.120989276.1722010158; GSIDsNOgpdeOrS4Q=f3ff6075-dc97-4ed5-b07a-1fff72c62d6a; STSIDsNOgpdeOrS4Q=517e91a6-54f0-4908-9c84-6e7f47781f00; _vt_shop=1363; _vt_user=3539079539495594_1_false_false; wingify_donot_track_actions=0; addshoppers.com=2%7C1%3A0%7C10%3A1722010160%7C15%3Aaddshoppers.com%7C44%3ANjgyZWI4OTVlYjBjNDlmYWI1ZmY1ZTkzYThiM2FhOGM%3D%7Cfa53527fd7d07ec839dca745f2cddd5886a59defb54bf163f9d901ec7b25bb54; PHPSESSID=olbksqeioad44h9an32obre6s9h9djd9ve8n87nasfqfs508u295eqeg67v7qouu; test-cookie=1; non_us_user=true; cart_items=true; comm100_visitorguid_1000443=5bad556e-99a8-40dc-a1c7-d4b0eef2b98c; _hjSessionUser_337611=eyJpZCI6IjkxOWJmMjk0LTExYzItNTQwMS04MGZkLTViZTA1MmZjZGFlYSIsImNyZWF0ZWQiOjE3MjIwMTAxNTc1NjUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_337611=eyJpZCI6IjY1ZGRlOTZiLTJiODktNDk0NS1iYzUyLTRhN2Q5NWFlNWRiZSIsImMiOjE3MjIyMTQzODU1NjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; ltk-suppression-ffaa860e-5be2-436a-9566-c9070ef41923=1; offers-tier-sNOgpdeOrS4Q=FS; _vuid=f3d271e4-d87d-445a-a887-0a1fb59cdea6; CYB_ID=3539079539495594; _ga_72KR0PQCFV=GS1.1.1722214379.2.1.1722214393.46.0.0; cybFalseID=1; CYB_AB=0; cybSessionID=1",
        #     "Origin": "https://www.bestcigarprices.com",
        #     "Priority": "u=0, i",
        #     "Referer": "https://www.bestcigarprices.com/?__cf_chl_tk=4uxRQLHBoZvRPDOqA4pIhbHqwe0.KFeQCp6giOtL9Xc-1722010143-0.0.1.1-3775",
        #     "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        #     "Sec-Ch-Ua-Arch": "x86",
        #     "Sec-Ch-Ua-Bitness": "64",
        #     "Sec-Ch-Ua-Full-Version": "126.0.6478.183",
        #     "Sec-Ch-Ua-Full-Version-List": '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Google Chrome";v="126.0.6478.183"',
        #     "Sec-Ch-Ua-Platform": "macOS",
        #     "Sec-Ch-Ua-Platform-Version": "13.4.0",
        #     "Sec-Fetch-Dest": "document",
        #     "Sec-Fetch-Mode": "navigate",
        #     "Sec-Fetch-Site": "same-origin",
        #     "Upgrade-Insecure-Requests": 1,
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        # }

        # headers = {
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        #     "Accept-Language": "en-PK,en-US;q=0.9,en;q=0.8",
        #     "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        #     "Sec-Ch-Ua-Platform": "macOS",
        #     "Sec-Ch-Ua-Platform-Version": "13.4.0",
        #     "Upgrade-Insecure-Requests": "1",
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        # }

        yield scrapy.Request(url= 'https://www.bestcigarprices.com/cigar-directory/cigars/', callback=self.parse)

    def parse(self, response):

        # f = open("test.html", "a")
        # f.write(str(response.body))
        # f.close()

        item_container = response.css('#main_item_container')
        print(response.text)

        # if item_container:
        print("********************************************************\n\n\n")
            # print(item_container)

        print(len(item_container.css('.item').getall()))
