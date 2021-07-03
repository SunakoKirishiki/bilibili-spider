import requests
from lxml import etree
import os
url='https://pic.netbian.com/4kmeinv/'
if not os.path.exists("C:\\Users\\Administrator\\Desktop\\girl"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\girl")
headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
ret=requests.get(url=url,headers=headers)
ret.encoding="gbk"
ret=ret.text
tree=etree.HTML(ret)
ret=tree.xpath('//ul[@class="clearfix"]/li')
for li in ret:
    pic_url="https://pic.netbian.com"+li.xpath('./a/img/@src')[0]
    pic_name=li.xpath('./a/img/@alt')[0]+".jpg"
    path="C:\\Users\\Administrator\\Desktop\\girl\\"+pic_name
    ret = requests.get(url=pic_url, headers=headers).content
    with open(path,"wb") as pic:
        pic.write(ret)
    print("图片保存完成")
