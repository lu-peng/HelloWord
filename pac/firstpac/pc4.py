'''
利用parse模拟post发送请求
分析百度词典
打开F12 发现每敲一个字母都有请求
发现请求地址是 https://fanyi.baidu.com/sug
发现formdata的内容是girl
检查返回内容格式是json 需要引入json包
'''
from urllib import request,parse
import json
'''
大致流程 利用data，然后url打开
返回一个json格式的结果
结果就是girl的解释
'''
base_url = 'https://fanyi.baidu.com/sug/'

#存放用来模拟的form的数据一定是dict

data={'kw':'girl'}
data = parse.urlencode(data).encode('utf-8')
print(type(data))
headers = {
    #因为使用post，则至少请求头应该包含Content-Length字段
    'Contnet-Length': len(data)
}

#有了headers 和data和url 就可以发送请求了

req = request.Request(base_url, data=data, headers=headers)
rsp = request.urlopen(req)

json_data=rsp.read().decode('utf-8')

print(json_data)
#把json转换成字典类型输出
json_data = json.loads(json_data)
print(json_data)

for item in  json_data['data']:
    print(item['k'],'---',item['v'])
