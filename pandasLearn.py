
import pandas as pd

import requests
from bs4 import BeautifulSoup
baseUrl = 'http://www.11315.com/ranklist/xygc-1'
def requestRankList(url):
    request = requests.get(baseUrl)
    soup = BeautifulSoup(request.text,'html5lib')
    items = soup.select('body > div.g-bd.f-cb.mt10 > div.g-mn > div.f-cb.borgray.mt10 > div > div.pb20 > table > tbody > tr')
    infoList = []
    
    for item in items:
        dic = {'name':item.select('td')[1].text,'area':item.select('td')[2].text,'url':item.select('td')[3].text}
        infoList.append(dic)
    df = pd.DataFrame(infoList,columns = ['name','area','url'])
    print(df)
    df.to_csv('file_name.tsv', sep='\t', encoding='utf-8')

def main():
    requestRankList(baseUrl)

if __name__ == '__main__':
    main()
    
