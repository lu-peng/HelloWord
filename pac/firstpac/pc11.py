'''
cookie作为一个变量打印出来
'''
from urllib import request,parse
from http import cookiejar

#1、创建cookie实例
cookie = cookiejar.CookieJar()
#2、创建cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#3、创建http处理器
http_handler = request.HTTPHandler()
#创建https处理器
https_handler = request.HTTPSHandler()
# 创建opener处理器
opener = request.build_opener(cookie_handler,http_handler,https_handler)

def login():
    url='http://www.renren.com/PLogin.do'
    data = {
        'email':'15882331340',
        'password':'lp123456'
    }
    data=parse.urlencode(data).encode('utf-8')
    headers = {
        'Content-Length':len(data)
    }
    req=request.Request(url,data=data,headers=headers)
    rsp=opener.open(req)

if __name__ == '__main__':
    '''
    执行完login（）后会得到授权后的cookie
    打印出cookie
    '''
    login()
    print(cookie)
    #print(type(cookie))
    for item in cookie :
        print(item)
       # print(type(item))
        for i in dir(item):
            print(i)