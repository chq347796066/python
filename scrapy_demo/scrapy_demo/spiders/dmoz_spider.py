import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D3%A1%B6%C8%C3%C0%C5%AE&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111",
    ]

    def parse(self, response):
        print(response)
        for sel in response.xpath("//img[@class='main_img']"):
            url=sel.xpath("/@src").extract()
            print("url: %s"%url)

