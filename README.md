# mattzheng/BaiduSpider解析
[fifths/python_baike_spider](https://github.com/fifths/python_baike_spider)，对于新手来说不太友好... 但是功能强大，目前
该库可以实现：百度百科、百度词典的爬取。

必要的库：**beautifulsoup4**

    pip install beautifulsoup4


## 1、baike_spider模块：百度百科

 - 功能：输入URL
 - 输出：HTML网址
   （详情见[output1.html](https://github.com/mattzheng/BaiduSpider/blob/master/baike_spider/output1.html)）
 - 主文件：[spider_main.py](https://github.com/mattzheng/BaiduSpider/blob/master/baike_spider/spider_main.py)

我这里对原作者的内容进行简单修改，可以指定路径保存 + 保存名称。

```
root_url = "http://baike.baidu.com/view/21087.htm"
save_path = './baike_spider/'
filename = 'output2.html'
obj_spider = SpiderMain()
obj_spider.craw(root_url,filename,save_path)
```


## 2、dict_spider模块：百度字典
主要用来解析百度词典：
![这里写图片描述](https://github.com/mattzheng/BaiduSpider/blob/master/dict_spider/dict_baidu.png?raw=true)

```
word='人'
values = {
    'wd': word,
    'ptype': 'char'
}
data = urllib.parse.urlencode(values)
root_url = "http://dict.baidu.com/s?" + data + '#'
obj_spider = SpiderMain()
obj_spider.craw(root_url)
```
生成的链接为： `'http://dict.baidu.com/s?ptype=char&wd=%E4%BA%BA#'`
