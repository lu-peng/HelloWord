'''
将cookie保存到文件
用MozillaCookieJar
'''
from urllib import request,parse
from http import cookiejar

filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(cookie_handler,http_handler,https_handler)

def login():
    url = 'http://www.renren.com/PLogin.do'
    data = {
        'email':'15882331340',
        'password':'lp123456'
    }
    data = parse.urlencode(data).encode('utf-8')
    headers = {
        'Content-Length':len(data)
    }
    req=request.Request(url,data=data,headers=headers)
    rsp=opener.open(req)
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()
