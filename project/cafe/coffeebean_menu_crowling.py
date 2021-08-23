
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
client = MongoClient('localhost', 27017)
db = client.dbsparta

url_list=[13,14,18,17,12,11,24,26] # 음료 카테고리 url 코드
page=[3,1,2,1,1,1,1,2] # 카테고리별 페이지
num=0
for o in url_list:
    for z in range(page[num]):
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url = 'https://www.coffeebeankorea.com/menu/list.asp?page='+str(z+1)+'&category='+str(o)+'&category2=1'
        data = requests.get(url,headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        trs = soup.select('#contents > div > div > ul>li')
        a=1
        for tr in trs:
            drink_info = dict()
            t = ':nth-child('+str(a)+') >'
            drink_info['img_url'] = 'https://www.coffeebeankorea.com/'+tr.select_one(t+'figure > img')['src']
            drink_info['name'] = tr.select_one(t + 'dl > dt > span.kor').text
            drink_info['kcal'] = tr.select_one(t + ' div > dl.bg1 > dt').text
            drink_info['sat_FAT'] = tr.select_one(t + ' div > dl.bg2 > dt').text
            drink_info['sodium'] = tr.select_one(t + ' div > dl.bg3 > dt').text #나트륨
            drink_info['chabo'] = tr.select_one(t + ' div > dl.bg4 > dt').text #탄수화물
            # 카페인 항목이 없을 때는 값 0 넣어줌
            if (tr.select_one(t + ' div > dl.bg5 > dt') is None):
                drink_info['caffeine'] = '0'
            else:
                drink_info['caffeine'] = tr.select_one(t + ' div > dl.bg5 > dt').text
            a+=1

            db.coffeebean.insert_one(drink_info)
    num+=1



