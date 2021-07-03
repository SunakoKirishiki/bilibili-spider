import scrapy
from scrapypro.items import ScrapyproItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E8%89%BE%E7%91%9E%E6%80%9D%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/20529447?fr=aladdin']

    def parse(self, response):

        div=response.xpath('/html/body/div[3]/div[2]/div/div[1]/div[4]/div//text()').extract()
        ret="".join(div)
        item=ScrapyproItem()
        item['ret']=ret
        yield item
