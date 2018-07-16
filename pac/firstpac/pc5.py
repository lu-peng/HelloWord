'''
访问url 捕获异常
'''
from urllib import request,error

if __name__ == '__main__' :
    url = 'http://www.baidu.com/'
    try:
        req=request.Request(url)
        rsp=request.urlopen(req)
        html=rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HTTPErroe: {0}".format(e.reson))
    except error.URLError as e:
        print("URLError: {0}".format(e.reson))
    except Exception as e:
        print(e)