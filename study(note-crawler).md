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
    -   案例：
            
            '''
            使用urllib.request请求一个网页内容，并把内容打印出来
            '''

            from urllib import request  # 导入urllib.request
            if __name__ == '__main__':
                url = "https://sou.zhaopin.com/?jl=586&kw=python&kt=3"
                # 打开相应url并把相应页面作为返回
                rsp = request.urlopen(url)
            
                html = rsp.read()   # 把返回的结果读取出来,读取出来的内容类型为bytes
                print(type(html))
            
                # 如果想把bytes内容转换成字符串，需要解码
                html = html.decode("utf-8")
            
                print(html)

-   网页编码问题解决
    -   chardet：可以自动检测页面文件的编码格式，但是未必正确
    -   需要安装：conda install chardet
    -   案例：
    
            '''
            利用request下载页面
            自动检测页面编码
            '''
            
            import urllib
            import chardet
            from urllib import request
            
            if __name__ == '__main__':
                url = "http://jiaren.org/2017/08/17/aiqing-375/"
                rsp = urllib.request.urlopen(url)
            
                html = rsp.read()
            
                # 利用chardet自动检测
                cs = chardet.detect(html)
                print(type(cs))
                print(cs)
            
                html = html.decode(cs.get("encoding","utf-8")) # 使用get取值保证不会出错
                print(html)

-   urlopen的返回对象
    -   案例：
    
            '''
            利用request下载页面
            自动检测页面编码
            '''
            
            import urllib
            import chardet
            from urllib import request
            
            if __name__ == '__main__':
                url = "http://jiaren.org/2017/08/17/aiqing-375/"
                rsp = urllib.request.urlopen(url)
                print(type(rsp))
                print(rsp)
            
                print("URL: {0}".format(rsp.geturl()))
                print("Info: {0}".format(rsp.info()))
                print("Code: {0}".format(rsp.getcode()))
            
                html = rsp.read()
                                       
                html = html.decode()  # 使用get取值保证不会出错
    
    -   geturl：返回请求对象的url
    -   info：请求反馈对象的meta信息
    -   getcode：返回的http code
-   request.data的使用
    -   访问网络的两种方法
        -   get：
            -   利用参数给服务器传递信息
            -   参数为dict，然后用parse编码
            -   案例：
        
                from urllib import request, parse
                '''
                掌握对url进行参数编码的方法
                需要使用parse模块
                '''
                
                if __name__ == '__main__':
                    url = "http://www.baidu.com/s？"
                    wd = input("Input your keyword:")
                
                    # 要想使用data，需要使用字典结构
                    qs = {
                        "wd": wd
                    }
                
                    # 转换url编码
                    qs = parse.urlencode(qs)
                    print(qs)
                
                    fullurl = url + qs
                    print(fullurl)
                
                    # 如果直接用可读的带参数的url，是不能访问的
                    fullurl = "http://www.baidu.com/s?wd=大熊猫"
                    rsp = request.urlopen(fullurl)
                
                    html = rsp.read()
                
                    # 使用get取值保证不会出错
                    html = html.decode()
                
                    print(html)
                    
        -   post：
            -   一般向服务器传递参数使用
            -   post是把信息自动加密处理
            -   我们如果像使用post信息，需要用到data参数
            -   使用post，意味着http的请求头里可能需要更改：
                -   Content-Type：application/x-www.form-urlencode
                -   Content-Length：数据长度
                -   简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            -   urllib.parse.urlencode可以自动将字符串自动转换成上面的格式
        
                    
                    