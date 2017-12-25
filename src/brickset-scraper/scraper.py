
"""
https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
https://en.wikipedia.org/wiki/XPath

"""
import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = ['http://brickset.com/sets/year-2017']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            PRICE_SELECTOR = './/dl[dt/text() = "RRP"]/dd/text()'
            TAGS_SELECTOR = './/div[@class="tags"]/a/text()'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
                'price': brickset.xpath(PRICE_SELECTOR).extract_first(),
                'tags': brickset.xpath(TAGS_SELECTOR).extract()
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

