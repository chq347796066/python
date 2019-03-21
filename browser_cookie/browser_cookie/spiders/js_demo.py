import requests
from scrapy.selector import Selector

#渲染地址端口
splash_url="http://localhost:8050/render.html"
args={"url":"http://quotes.toscrape.com/js/","timeout":5,"image":0}
reponse=requests.get(splash_url,params=args)
sel=Selector(reponse)
ets = sel.css("div.quote span.text::text").extract()
for et in ets:
    print("et:%s"%et)
