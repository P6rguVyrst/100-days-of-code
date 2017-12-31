
"""
https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
https://en.wikipedia.org/wiki/XPath

"""
import re
import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = ['http://minecraft-server-list.com/']

    def extract_item(self, item):
        data = dict(
            _id = item.css('td ::attr(id)').extract_first(),
            _href = item.css('a ::attr("href")').extract_first(),
            _tags = item.xpath('span[@class="buttonsmall black size10"]/text()').extract(),
            _ip = item.xpath('span/input/@value').extract_first(),
            _version = item.xpath('span[@class="buttonsmall black size10"][contains(., "Version")]/text()').extract_first(),
        )
        if data['_version']:
            data['_version'] = self.remove_prefix(data['_version'].lower(), 'version: ')
        data['_tags'] = [tag for tag in data['_tags'] if not tag.lower().startswith('version')]

        return data

    def normalize_whitespace(self, str):
        str = str.strip()
        str = re.sub(r'\s+', ' ', str)
        return str

    def parse(self, response):

        SET_SELECTOR = '//div[@class="serverdatadiv1"]/table/tr/td'
        for selector in response.xpath(SET_SELECTOR):
            SUBSET2_SELECTOR = '//*[@class="n2"]'
            SUBSET3_SELECTOR = '//*[@class="n3"]'
            server = {}
            for item in selector.xpath(SUBSET2_SELECTOR):
                data = self.extract_item(item)
                server['id'] = data['_id']
                server['href'] = data['_href']
                server['tags'] = data['_tags']
                server['version'] = data['_version']
                server['ip'] = data['_ip']
                for item in selector.xpath(SUBSET3_SELECTOR):
                    _players = item.css('span ::text').extract_first()
                    if _players:
                        _players = self.remove_prefix(_players.lower(), 'players:')
                        _players = self.normalize_whitespace(_players)
                    server['players'] = _players

                #print(server)
                yield server

        NEXT_PAGE_SELECTOR = '//div[@class="paginate paginate-dark pagination-wrapper"]/ul/li/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract()[-2]
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def remove_prefix(self, text, prefix):
        return text[text.startswith(prefix) and len(prefix):]
