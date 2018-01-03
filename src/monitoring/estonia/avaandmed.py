import scrapy
# API PATHS: https://www.ametlikudteadaanded.ee/avalik/uriotsing

BASE_URI = 'https://ametlikudteadaanded.ee/ee/-'
"""
PATHS = {
    'data': [
        {'uri': f'{BASE_URI}/enapakkumine-myyk', 'tags': ['auction', 'sale']},
        {'uri': f'{BASE_URI}/halduslepingud', 'tags': ['government', 'contracts']},
        {'uri': f'{BASE_URI}/kinnisturaamat', 'tags': ['property', 'real-estate']},
        {'uri': f'{BASE_URI}/konkurents', 'tags': ['']},
        {'uri': f'{BASE_URI}/majandustegevus', 'tags': []},
        {'uri': f'{BASE_URI}/riigivara', 'tags': []},
        {'uri': f'{BASE_URI}/konkurents', 'tags': []},

    ]
}

for item in PATHS['data']:
    print(item)
"""




class CrawlEstonia(scrapy.Spider):
    name = 'Estonia'
    start_urls = ['https://www.ametlikudteadaanded.ee/avalik/uriotsing']

    def parse(self, response):
        SET_SELECTOR = './/div[@class="col-md-12"]/table/tbody/tr'#tr/td/text()'
        for brickset in response.xpath(SET_SELECTOR):
            SEL = 'td ::text'
            item = brickset.css(SEL).extract()[-1]
            # EACH ITEM CAN BE MONITORED. SEE URI's above.
            # SELECT ONLY tr where <td style="font-weight:bold"> - to avoid subcategories and duplicate entries.


            #yield {
            #    'name': brickset.css(NAME_SELECTOR).extract_first(),
            #}


