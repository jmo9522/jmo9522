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
    html = html.decode()
    print(html)

