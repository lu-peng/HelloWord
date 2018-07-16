'''
通过第一次登陆人人网保存cookie后再次登陆
第一次登陆后自动管理cookie
'''

from urllib import request,parse
from http import cookiejar
#首先创建cookiejar实例
cookie = cookiejar.CookieJar()
#生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#生成http管理器
http_handler = request.HTTPHandler()
#生成Https管理器
https_handler = request.HTTPSHandler()

#创建opener请求管理器
opener = request.build_opener(cookie_handler,http_handler,https_handler)

def login():
    '''
     负责通过用户名和密码登陆人人网
    :return:
    '''
    url='http://www.renren.com/PLogin.do'
    data={
        'email':'15882331340',
        'password':'lp123456'
    }
    data = parse.urlencode(data).encode('utf-8')
    headers={
        'Content-Length':len(data)
    }

    req = request.Request(url,data=data,headers=headers)
    #rsp = request.urlopen(req)
    #html = rsp.read().decode()
    rsp = opener.open(req)

def getHomePage():
    url='http://www.renren.com/966959406/profile'
    #如果已经执行了login函数，则opener已经包含了cookie值
    rsp=opener.open(url)
    html = rsp.read().decode()

    with open('rsp2.html','w',encoding='utf-8') as f:
        f.write(html)
if __name__ == '__main__':
    login()
    getHomePage()