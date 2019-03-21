import scrapy
from scrapy_splash import SplashRequest

class BaiduSpider(scrapy.Spider):
    name = 'baidu_image'
    start_urls=["https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D3%A1%B6%C8%C3%C0%C5%AE&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,args={"images":0,"timeout":3})

    def parse(self, response):
        for box in response.css("div.imgbox"):
            url=box.css("a img::attr(src)").extract_first()
            print("url:%s"%url)
            yield {"image_urls":[url],}