import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import requests
import os


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


def download_vcode(pic_url):
    try:
        url = pic_url  # '识别图片URL地址'

        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
        resp = requests.get(url, headers=headers, verify=False)
        file_name = 'C:\\Users\\Administrator\\Desktop\\验证码\\lianzhong_vcode.png'
        with open(file_name, 'wb') as f:
            f.write(resp.content)
    except Exception as e:
        print(e)


if not os.path.exists("C:\\Users\\Administrator\\Desktop\\验证码"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\验证码")

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)

try:
    driver.get("https://qzone.qq.com/")
except selenium.common.exceptions.TimeoutException:
    print("time out of 30 s")
    driver.execute_script('window.stop()')

driver.switch_to.frame('login_frame')
a = driver.find_element_by_id('switcher_plogin')
a.click()
time.sleep(3)
u = driver.find_element_by_id('u')
u.send_keys(QQ)
time.sleep(1)
p = driver.find_element_by_id('p')
p.send_keys(密码)
time.sleep(1)
button = driver.find_element_by_id('login_button')
button.click()
time.sleep(5)
driver.switch_to.frame('tcaptcha_iframe')
img = driver.find_element_by_id('slideBg')
img.screenshot("C:\\Users\\Administrator\\Desktop\\验证码\\vcode.png")
# 这是使用requests下载验证码图片的代码
# pic_url = img.get_attribute("src")
# download_vcode(pic_url)
# TODO
