#coding=utf-8
import requests
import json
from lxml import etree

ip_url="http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=100026&port=11&pack=159285&ts=1&ys=1&cs=1&lb=1&sb=0&pb=45&mr=1&regions="

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

    }

ret=requests.get(url=ip_url,headers=headers).json()
ip=ret['data'][0]['ip']
port=ret['data'][0]['port']
targetUrl = "https://www.baidu.com/s?wd=ip"

#代理服务器
proxyHost =ip
proxyPort = port

proxyMeta = "http://%(host)s:%(port)s" % {

    "host" : proxyHost,
    "port" : proxyPort,
}


proxies = {

    "http"  : proxyMeta,
    "https"  : proxyMeta
}
print(proxies)
resp = requests.get(url=targetUrl,headers=headers,proxies=proxies).text
with open("C:\\Users\\Administrator\\Desktop\\ip.html", "w", encoding='utf-8') as file:
    file.write(resp)