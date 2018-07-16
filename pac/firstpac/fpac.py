import urllib.request

from pip._vendor import chardet
'''请求网址 urllib.resquest.urlopen'''
response = urllib.request.urlopen('https://www.cnblogs.com/zhaof/p/6910871.html')
print(type(response))
'''
geturl 返回请求对象的url
info 请求反馈对象的meta信息
getcode 返回的httpcode
'''
print('返回的url：{0}'.format(response.geturl()))
print('返回的info：%s' % (response.info()))
print("返回的code：{0}".format(response.getcode))

rspstr = response.read()
'''
自动检测网页编码 利用chardet检测
'''
datecode = chardet.detect(rspstr)
print(type(datecode))
print(datecode.get('encoding'))

'''print(rspstr.decode('utf-8'))
'''