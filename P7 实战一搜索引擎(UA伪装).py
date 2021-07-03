# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests



if __name__ == '__main__':
    url='https://www.sogou.com/web'
    #UA伪装
    headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    kw=input('输入查询内容\n')
    param={
        'query':kw
    }
    ret=requests.get(url=url,params=param,headers=headers)
    ret=ret.text
    with open("C:\\Users\\Administrator\\Desktop\\1.html","w",encoding='utf-8') as file:
        file.write(ret)



