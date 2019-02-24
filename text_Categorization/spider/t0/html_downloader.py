import string
from urllib import request
from urllib.parse import quote
import chardet

class HtmlDownloader(object):
    def __init__(self):
        pass

    def download(self, url):
        if url is None:
            return None

        #header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER' }
        #url_ = request.Request(url, headers=header)
        url_ = request.Request(url)
        response = request.urlopen(url_)

        if response.getcode() != 200:
            return None

        # 自动识别网页的编码格式，然后转换成utf-8格式
        html = response.read()
        mychar = chardet.detect(html)
        #print(mychar)
        bianma = mychar['encoding']
        if bianma == 'utf-8' or bianma == 'UTF-8':
            html = html.decode('utf-8', 'ignore').encode('utf-8')
        else:
            html = html.decode('gb2312', 'ignore').encode('utf-8')
        #print(chardet.detect(html))

        return html
