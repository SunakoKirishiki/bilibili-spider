import requests
from lxml import etree
import os
import random
from multiprocessing.dummy import Pool
import re
url='https://www.pearvideo.com/category_4'
if not os.path.exists("C:\\Users\\Administrator\\Desktop\\梨视频"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\梨视频")
headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
ret=requests.get(url=url,headers=headers)
ret.encoding="utf-8"
ret=ret.text
tree=etree.HTML(ret)
ret=tree.xpath('//li[@class="categoryem"]')
参数字典=[]
for li in ret:
    pic_name=li.xpath('./div/a/div[2]/text()')[0]
    pic_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    video_url="https://www.pearvideo.com/videoStatus.jsp?"
    id=li.xpath('./div/a/@href')[0][-7:]
    params={
        'contId': id,
        'mrd': str(random.random())
    }
    li_headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': pic_url
    }
    path="C:\\Users\\Administrator\\Desktop\\梨视频\\"+pic_name+".mp4"
    ret=requests.get(url=video_url,headers=li_headers,params=params).json()['videoInfo']['videos']['srcUrl']
    ret_ex=ret.split("/")
    substr='cont-'+str(id)+"-"
    each_re="^.*?-"
    ret_ex[-1]=re.sub(each_re,substr,ret_ex[-1])
    true_url=ret_ex[0]+"/"+ret_ex[1]+"/"+ret_ex[2]+"/"+ret_ex[3]+"/"+ret_ex[4]+"/"+ret_ex[5]+"/"+ret_ex[6]
    dic={
        'name':path,
        'url':true_url
    }
    参数字典.append(dic)

def 获取视频(字典):
    地址=字典['url']
    路径=字典['name']
    print("下载中", 路径)
    ret = requests.get(url=地址, headers=headers).content
    with open(路径, "wb") as video:
        video.write(ret)
    print("下载结束", 路径)

pool=Pool(4)
pool.map(获取视频,参数字典)
pool.close()
pool.join()





