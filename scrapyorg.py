#encoding utf-8
import scrapy
from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory

DOWNLOADER_CLIENTCONTEXTFACTORY = 'scrapyorg.contextfactory.MyClientContextFactory'

class MyClientContextFactory(ScrapyClientContextFactory):
    def __init__(self):
        self.method = SSL.SSLv23_METHOD  # or SSL.SSLv3_METHOD
class org(scrapy.Spider):
    name = 'scrapyorg'
    start_urls = ['https://doc.scrapy.org/en/latest/topics/selectors.html?highlight=extract()']
    def parse(self, response):
       item = response.xpath('//*[@class="btn btn-neutral float-right"]/@href')
       print('$$$$$$$')
       if item:
           print(item.extract())
           yield scrapy.Request(item.extract(),callback=self.next_parse)
    def next_parse(self,response):
        print(123)