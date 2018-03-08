import os,sys
#sys.path.append('E:\matt\crawler\python_baike_spider-master')
from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url,filenames,save_path):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" %(count, new_url))
                html_cont = self.downloader.download(new_url)  # response.read()
                new_urls, new_data = self.parser.paser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html(filename = filenames,path = save_path)  # 全局


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    #save_path = None  # 全局
    save_path = 'E:\\matt\\crawler\\python_baike_spider-master\\baike_spider\\'
    filename = 'output2.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url,filename,save_path)
