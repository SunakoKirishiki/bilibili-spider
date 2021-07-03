import requests
import os
import re
if __name__ == '__main__':
    if not os.path.exists("C:\\Users\\Administrator\\Desktop\\pic"):
        os.mkdir("C:\\Users\\Administrator\\Desktop\\pic")
    url='https://www.qiushibaike.com/imgrank/'
    #UA伪装
    headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    ret=requests.get(url=url,headers=headers).text

    img="<div class=\"thumb\">.*?<img src=\"(.*?)\" alt=\".*?</div>"
    img_list=re.findall(img,ret,re.S)
    for pic in img_list:
        pic='https:'+pic
        ret=requests.get(url=pic,headers=headers).content
        imgpath="C:\\Users\\Administrator\\Desktop\\pic\\"+pic.split("/")[-1]
        with open(imgpath,"wb") as picture:
            picture.write(ret)
        print("下载完成")


