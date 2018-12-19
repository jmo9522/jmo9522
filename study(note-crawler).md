#   爬虫准备工作
-   参考资料
    -   Python网络数据采集·图灵工业出版
    -   精通Python爬虫框架Scrapy·人民邮电出版社
    -   [Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    -   [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
-   前提知识
    -   url
    -   http协议
    -   web前端·html，css，js
    -   ajax
    -   re，xpath
    -   xml
#   爬虫简介
-   爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
-   两大特征
    -   能按作者要求下载数据或者内容
    -   能自动在网络上流窜
-   三大工作步骤
    -   下载信息
    -   提取正确的信息
    -   根据一定的规则自动跳到另外的网页上执行上两步内容
-   爬虫分类
    -   通用爬虫
    -   专用爬虫（聚焦爬虫）
-   Python网络包简介
    -   Python2.x：urllib, urllib2, urllib3, httplib, httplib2, requests
    -   Python3.x：urllib, urllib3, httplib2, requests
    -   Python2中常用：urllib 和 urllib2配合使用，或者requests
    -   Python3中常用：urllib，requests
#   urllib
-   包含模块
    -   urllib.requests: 打开和读取urls
    -   urllib.error: 包含urllib.requests产生的常见错误，使用try捕捉
    -   urllib.parse: 包含解析url的方法
    -   urllib.robotparse: 解析robots.txt文件
    