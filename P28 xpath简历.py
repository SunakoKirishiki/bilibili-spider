import requests
from lxml import etree
import os

def 批量下载(page_num):
    if page_num==1:
        url='https://sc.chinaz.com/jianli/free.html'
    else:
        url="https://sc.chinaz.com/jianli/free_"+str(page_num)+".html"
    ret = requests.get(url=url, headers=headers)
    ret.encoding = "utf-8"
    ret = ret.text
    tree = etree.HTML(ret)
    ret = tree.xpath('//div[@id="container"]/div')
    for li in ret:
        jl_url = "https:" + li.xpath('./a/@href')[0]
        name = li.xpath('./a/img/@alt')[0] + ".rar"
        ret = requests.get(url=jl_url, headers=headers)
        ret.encoding = "utf-8"
        ret = ret.text
        li_tree = etree.HTML(ret)
        download_url = li_tree.xpath('//div[@class="clearfix mt20 downlist"]//li[3]/a/@href')[0]
        ret = requests.get(url=download_url, headers=headers).content
        path = "C:\\Users\\Administrator\\Desktop\\简历\\" + name
        with open(path, "wb") as pic:
            pic.write(ret)
        print("模板下载")

if not os.path.exists("C:\\Users\\Administrator\\Desktop\\简历"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\简历")
headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
批量下载(2)

