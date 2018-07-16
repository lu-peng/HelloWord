'''
没有cookie登陆案例
'''
from urllib import request,error
from pip._vendor import chardet
if __name__ == '__main__':
    url = 'http://www.renren.com/966959406/profile'
    rsp = request.urlopen(url)
    html = rsp.read()
    print(type(html))

    datacode = chardet.detect(html)
    print(datacode)
    print(datacode.get('encoding'))
    with open('rsp.html','w',encoding='utf-8') as f:
        f.write(html.decode())

