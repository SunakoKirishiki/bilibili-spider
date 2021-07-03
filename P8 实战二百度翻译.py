import requests
import json



if __name__ == '__main__':
    post_url='https://fanyi.baidu.com/sug'
    #UA伪装
    headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    kw=input('输入查询内容\n')
    data={
        'kw':kw
    }
    ret = requests.post(url=post_url, data=data, headers=headers)
    ret=ret.json()
    with open("C:\\Users\\Administrator\\Desktop\\1.json","a",encoding='utf-8') as file:
        json.dump(ret,fp=file,ensure_ascii=False)
