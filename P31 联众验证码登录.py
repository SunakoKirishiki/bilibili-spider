#古诗文网模拟登陆
#使用联众打码平台，需要自己补全用户名密码

import requests
from lxml import etree
import os
import json
def query(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type, tools_token, workerTipsId):
    '''
            main() 参数介绍
            api_username    （API账号）             --必须提供
            api_password    （API账号密码）         --必须提供
            file_name       （需要识别的图片路径）   --必须提供
            api_post_url    （API接口地址）         --必须提供
            yzm_min         （识别结果最小长度值）        --可空提供
            yzm_max         （识别结果最大长度值）        --可空提供
            yzm_type        （识别类型）          --必须提供
            tools_token     （V1软件Token）     --必须提供
            worker_tips_id   (识别者贴边提示模板ID)  --可空提供
    '''
    # api_username =
    # api_password =
    # file_name = 'c:/temp/lianzhong_vcode.png'
    # api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    # yzm_min = '1'
    # yzm_max = '8'
    # yzm_type = '1303'
    # tools_token = api_username
    # worker_tips_id = '0'

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': ('1.png', open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token,
        'worker_tips_id':workerTipsId
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    return r


def download_vcode(pic_url):
    try:
        url = pic_url   # '识别图片URL地址'

        headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
        resp = l.get(url, headers=headers, verify=False)
        file_name = 'C:\\Users\\Administrator\\Desktop\\验证码\\lianzhong_vcode.png'
        with open(file_name, 'wb') as f:
            f.write(resp.content)
    except Exception as e:
        print(e)
if not os.path.exists("C:\\Users\\Administrator\\Desktop\\验证码"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\验证码")
headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
url="https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx"
l=requests.session()
ret=l.get(url=url,headers=headers)
ret.encoding="utf-8"
ret=ret.text
tree=etree.HTML(ret)
ret="https://so.gushiwen.org"+tree.xpath('//div[@class="mainreg2"][1]/div[4]/img/@src')[0]
download_vcode(ret)
ret=query(联众用户名,联众密码,'C:\\Users\\Administrator\\Desktop\\验证码\\lianzhong_vcode.png','http://v1-http-api.jsdama.com/api.php?mod=php&act=upload','','','1001','50c7ed0376749c5e259e25730e9ab46b','')
ret=json.loads(ret.text)
login_url="https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx"
vcode=ret["data"]["val"]
data={
"__VIEWSTATE":"HMw03pJm9xqeVdcWhxRTmDrOzHEb0n8mY7z5w7D8Log5YVZwqXbTDbN2EYmUD0rO3Fk8hMumSXMnCDXBHg0Sfj38NJ5AJJpcM8h7Fyjtn3EeYp2VDdXpJR/M5ng=",
"__VIEWSTATEGENERATOR":"C93BE1AE",
"from":"http://so.gushiwen.org/user/collect.aspx",
"email":古诗文网用户名,
"pwd":古诗文网密码,
"code":vcode,
"denglu":"登录"
    
}
ret = l.post(url=login_url, data=data, headers=headers)
print(ret.status_code)
with open("C:\\Users\\Administrator\\Desktop\\验证码\\login.html", "w", encoding='utf-8') as file:
    file.write(ret.text)