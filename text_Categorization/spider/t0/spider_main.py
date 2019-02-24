from spider.t0 import url_manager, html_downloader, html_parser, html_outputer
import datetime


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 网页下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器
        self.count = 1

    def init_url(self, root_url):
        self.urls.add_new_url(root_url)
        try:
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls = self.parser.parse1(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
        except Exception as e:
            print(str(e))  # 根据报错信息提示错误

    def craw(self):
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                #print("craw %d : %s" % (self.count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                #if self.count >= 100000:
                #    break
                #print(self.count)
                self.count += 1

            except Exception as e:
                print(str(e))  # 根据报错信息提示错误


if __name__ == '__main__':

    obj_spider = SpiderMain()
    today = datetime.datetime.strptime('2017-06-20', '%Y-%m-%d')
    while obj_spider.count<=18000:
        root_url='http://www.chinanews.com/scroll-news/sh/'+str(today)[0:4]+'/'+str(today)[5:7] + str(today)[8:10]+'/news.shtml'
        obj_spider.init_url(root_url)
        obj_spider.craw()
        print(today)
        print(obj_spider.count)
        today = today + datetime.timedelta(days=-1)