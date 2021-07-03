import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
driver=webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chrome_options,options=option)
driver.get("https://www.baidu.com/")
print(driver.page_source)
time.sleep(2)
driver.quit()
