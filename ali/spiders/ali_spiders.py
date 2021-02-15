import scrapy
from ..items import AliItem

class AliSpider(scrapy.Spider):
    name = 'ali'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.start_urls = [self.url]

        super(AliSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        i = {}
        i['url'] = response.url
        return i