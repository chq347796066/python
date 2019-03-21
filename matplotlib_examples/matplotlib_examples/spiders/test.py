
from urllib.parse import urlparse
o = urlparse("https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22"
                 "nid%22%3A%22news_16182703442770107536%22%7D&n_type=0&p_from=1")
if __name__ == '__main__':
   print(o)
