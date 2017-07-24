from lxml import etree
import requests
import qqscrapy

Headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

baseUrl = 'https://search.damai.cn/search.html?ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&cty=%E5%8C%97%E4%BA%AC&order=1'

def getDamaiTickets():
    data = requests.get(baseUrl,headers = Headers)
    selector = etree.HTML(data.text)
    items = selector.xpath('//*[@class="search_img"]/a')

    for item in items:
        print('https:'+item.get('href'))


def main():
    # getDamaiTickets()
    qqscrapy()

if __name__ == '__main__':
    main()


