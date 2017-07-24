#encoding utf-8
import scrapy

class qqnewsSpider(scrapy.Spider):
    name = 'qqnewspider'
    start_urls = ['http://news.qq.com/society_index.shtml']

    def parse(self,response):
       
        for url in response.xpath('//*[@id="news"]/div/div/div/div/em/a/@href'):
            print('@@@@@@')
            print(type(url))
            print(type(url.extract()))
            list_a = response.urljoin(url.extract())        

            return scrapy.Request(list_a,callback = self.detailParse)
    def detailParse(self,response):
        print type(response.xpath('//div[@class="qq_article"]/div/h1/text()'))
        print type(response.xpath('//div[@class="qq_article"]/div/h1/text()').extract_first())

        pass
