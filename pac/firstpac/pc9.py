#========================================
'''
有cookie的登陆,手动录入cookie
'''
from urllib import request
if __name__ == '__main__':
    url = 'http://www.renren.com/966959406/profile'
    headers={}
    headers['Cookie']='anonymid=jjoejcdfb2hh2g; depovince=GW; _r01_=1; JSESSIONID=abcRddyPgLpEB7qloOJsw; ick=a9dd299b-2046-4368-ba3f-a8f6864e2426; XNESSESSIONID=55f4f28cc46f; jebecookies=39c7b99e-a17d-4ecb-859f-5976bcbed2d5|||||; ick_login=40441175-afa6-490a-94cd-2302ec48c946; _de=33DBFE3AAFE7BEF972D4F31474742CB5; p=66c388821bbe1d64709c6b24be1a09d26; first_login_flag=1; ln_uact=15882331340; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=8ad5610059b4c6abcc99a1e3e253e4616; societyguester=8ad5610059b4c6abcc99a1e3e253e4616; id=966959406; xnsid=5c560cbc; ver=7.0; loginfrom=null; Hm_lvt_4e5bdf78b2b9fcb88736fc67709f2806=1531753600,1531753768,1531754082; Hm_lpvt_4e5bdf78b2b9fcb88736fc67709f2806=1531754363; jebe_key=5b176c09-4c19-4945-ac81-bca2ff109f8e%7Ce400e4f4cf468d3247f27409b8745096%7C1531754832354%7C1; wp_fold=0'
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html=rsp.read().decode()

    with open('rsp.html','w',encoding='utf-8') as f:
        f.write(html)