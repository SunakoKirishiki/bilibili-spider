import requests
import lxml
import bs4
import os
url='https://www.shicimingju.com/book/sanguoyanyi.html'
if not os.path.exists("C:\\Users\\Administrator\\Desktop\\txt"):
    os.mkdir("C:\\Users\\Administrator\\Desktop\\txt")
headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
ret=requests.get(url=url,headers=headers).text.encode("iso-8859-1")
soup=bs4.BeautifulSoup(ret,'lxml')
li_list=soup.select('.book-mulu > ul > li ')
for li in li_list:
    li_url='https://www.shicimingju.com'+li.a['href']
    title=li.a.string
    ret = requests.get(url=li_url, headers=headers).text.encode("iso-8859-1")
    li_soup = bs4.BeautifulSoup(ret, 'lxml')
    li_ret=li_soup.find('div',class_='chapter_content').text
    path="C:\\Users\\Administrator\\Desktop\\txt\\"+title+".txt"
    with open(path,"w",encoding="utf-8") as txt:
        txt.write(li_ret)
    print(title,"finish")
