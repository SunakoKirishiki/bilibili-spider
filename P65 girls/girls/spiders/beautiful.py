import scrapy


class BeautifulSpider(scrapy.Spider):
    name = 'beautiful'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']
    url="http://www.521609.com/meinvxiaohua/list12%d.html"
    page_num=2

    def parse(self, response):
        li_list=response.xpath("/html/body/div[4]/div[2]/div[2]/ul/li")
        for li in li_list:
            ret=li.xpath("./a[2]//text()").extract_first()
            print(ret)
            if self.page_num<=11:
                new_url = format(self.url % self.page_num)
                self.page_num += 1
                yield scrapy.Request(url=new_url, callback=self.parse)


