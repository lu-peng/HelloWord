'''
访问url设置user-agent
'''

from urllib import request,error

if __name__ == '__main__':
    headers={}
    # 添加字典信息  dict[key]=value
    headers['User-Agent']='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (' \
                          'KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
    url = 'https://www.baidu.com/'

    try:
        req=request.Request(url,headers=headers)
        rsp=request.urlopen(req)
        html=rsp.read().decode()

        print(html)

    except error.HTTPError as e:
        print('Httperror:{0}'.format(e.reason))
    except error.URLError as e:
        print('Urlerror:{0}'.format(e.reason))
    except Exception as e:
        print('Exception:{0}'.format(e))