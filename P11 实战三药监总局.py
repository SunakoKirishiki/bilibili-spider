import requests
import json
if __name__ == '__main__':
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    #UA伪装
    headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }

    param={
        'on': 'true',
        'page':1,
        'pageSize':15,
        'productName':'',
        'conditionType':1,
        'applyname':'',
        'applysn':''
    }
    ret=requests.post(url=url,data=param,headers=headers)
    ret=ret.json()
    print(ret['list'][1]['ID'])

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    id=ret['list'][1]['ID']
    param = {
        'id': id
    }

    ret = requests.post(url=url, data=param, headers=headers)
    ret = ret.json()
    with open("C:\\Users\\Administrator\\Desktop\\1.json", "a", encoding='utf-8') as file:
        json.dump(ret, fp=file, ensure_ascii=False)
