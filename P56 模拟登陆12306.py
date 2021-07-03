#使用联众打码平台，需要自己补全用户名密码
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import requests
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
        'worker_tips_id': workerTipsId
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    return r

if not os.path.exists("C:\\Users\\Administrator\\Desktop\\验证码"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\验证码")

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)

try:
    driver.get("https://kyfw.12306.cn/otn/resources/login.html")
except selenium.common.exceptions.TimeoutException:
    print("time out of 30 s")
    driver.execute_script('window.stop()')
login=driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a")
login.click()
time.sleep(3)
pic=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/img")
pic.screenshot("C:\\Users\\Administrator\\Desktop\\验证码\\vcode.png")
ret=query(联众用户名,联众密码,'C:\\Users\\Administrator\\Desktop\\验证码\\vcode.png','http://v1-http-api.jsdama.com/api.php?mod=php&act=upload','','','1303','78349d14720113b2db27ddbc5054fc69','')
ret=json.loads(ret.text)['data']['val']
结果坐标=[]
if "|" in ret:
    ret=ret.split("|")
    for l in ret:
        l=l.split(",")
        结果坐标.append([int(l[0]),int(l[1])])
else:
    ret=ret.split(",")
    结果坐标.append([int(ret[0]), int(ret[1])])
print(结果坐标)
for e in 结果坐标:
    x=e[0]
    y=e[1]
    ActionChains(driver).move_to_element_with_offset(pic,x,y).click().perform()
    time.sleep(1)
driver.find_element_by_id("J-userName").send_keys(用户名)
time.sleep(1)
driver.find_element_by_id("J-password").send_keys(密码)
time.sleep(1)
driver.find_element_by_id("J-login").click()
time.sleep(10)
driver.quit()

