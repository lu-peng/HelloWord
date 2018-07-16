'''
使用代理访问url
'''

from urllib import request,error

if __name__ == '__main__':
    url='http://www.baidu.com'
    #-基本使用步骤
    #1、设置代理地址
    proxy = {'http':'171.10.31.73:8080'}
    #2、创建ProxyHandler
    proxy_hander = request.ProxyHandler(proxy)
    #3、创建Opener
    opener = request.build_opener(proxy_hander)
    #4、安装Opener
    request.install_opener(opener)

    #之后访问url就是使用代理服务器来进行访问的
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e.reason)
    except error.HTTPError as e:
        print(e.reason)
    except Exception as e:
        print(e)
