import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = ['https://poff.ee/est/filmid']

    def parse(self, response):
        SET_SELECTOR = '.movie-simple-titles'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h2 ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),

            }



