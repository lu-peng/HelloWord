#========================================
'''
利用parse发送get请求
'''
import urllib.request
from urllib import parse

url = 'http://www.baidu.com/s?'

wd=input("input your value:")

data = {"ind": wd}
data = parse.urlencode(data)
fullurl = url + data
print(fullurl)
rsp = urllib.request.urlopen(fullurl)
print(rsp.read().decode())
