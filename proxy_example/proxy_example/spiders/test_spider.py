import scrapy
from scrapy import Request
import json

class TestRandomProxySpider(scrapy.Spider):
    name = 'test_spider'

    def start_requests(self):
        for _ in range(100):
            yield Request("http://httpbin.org/ip",dont_filter=True)
            yield Request("https://httpbin.org/ip", dont_filter=True)


    def parse(self, response):
        yield {'proxy_ip':json.loads(response.text)['origin']}