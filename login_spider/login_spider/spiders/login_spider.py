

import scrapy
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains=['example.webscraping.com']

    start_urls = ['http://example.webscraping.com/user/profile']

    def parse(self, response):
        print("parse")
        keys=response.css('table lable::text').re('(.+):')
        values=response.css('table td.w2p_fw::text').extract()
        yield dict(zip(keys,values))

    login_url="http://example.webscraping.com/places/default/user/login"

    def start_requests(self):
        print("start_requests")
        yield Request(self.login_url,callback=self.login)

    def login(self,response):
        fd={"email":"chq347796066@126.com","password":"152965318"}
        yield FormRequest.from_response(response,formdata=fd,callback=self.parse_login)

    def parse_login(self,response):
        print("parse_login")
        if "海权" in response.text:
            yield from super().start_requests()
