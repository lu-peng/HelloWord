'''
cookie的读取
'''

from urllib import request,parse
from http import cookiejar
filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(cookie_handler,https_handler,http_handler)

def getHomePage():
    url='http://www.renren.com/966959406/profile'
    rsp=opener.open(url)
    with open('rsp3.html','w',encoding='utf-8') as f:
        f.write(rsp.read().decode())

if __name__ == '__main__':
    getHomePage()