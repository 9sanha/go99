
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가 / 옵션 추가 안하면 실시간으로 크롤링 하는 모습을 볼 수 있음
options.add_argument("headless")

# webdriver 실행
dr = webdriver.Chrome('E:/webdriver/chromedriver.exe', options=options)
# target page 접근
dr.get("https://www.starbucks.co.kr/menu/drink_list.do")
# html source 추출
html_source = dr.page_source

# BS4로 html parsing
soup = BeautifulSoup(html_source, 'html.parser')
# 원하는 항목의 데이터만 추출
products = soup.select('.product_list dd a')

# 제품 이름, 코드 추출 - url용 데이터
prod_cd = [[product.find('img')['alt'], product['prod'], product.find('img')['src']] for product in products]
# 결과 확인

res = []
for prod in prod_cd:
    drink_info = dict()
    code = prod[1]
    dr.get("https://www.starbucks.co.kr/menu/drink_view.do?product_cd={prod_code}".format(prod_code=code))
    html_src=dr.page_source
    soup = BeautifulSoup(html_src,'html.parser')

    # 용량 정보
    drink_info['volume'] = soup.select_one('.product_info_head #product_info01').get_text()
    # 제품 영양 정보
    drink_info['kcal'] = soup.select_one('.product_info_content .kcal dd').get_text()
    drink_info['sat_FAT'] = soup.select_one('.product_info_content .sat_FAT dd').get_text()
    drink_info['protein'] = soup.select_one('.product_info_content .protein dd').get_text()
    drink_info['fat'] = soup.select_one('.product_info_content .fat dd').get_text()
    drink_info['trans_FAT'] = soup.select_one('.product_info_content .trans_FAT dd').get_text()
    drink_info['protein'] = soup.select_one('.product_info_content .protein dd').get_text()
    drink_info['sodium'] = soup.select_one('.product_info_content .sodium dd').get_text()
    drink_info['sugars'] = soup.select_one('.product_info_content .sugars dd').get_text()
    drink_info['caffeine'] = soup.select_one('.product_info_content .caffeine dd').get_text()
    drink_info['cholesterol'] = soup.select_one('.product_info_content .cholesterol dd').get_text()
    drink_info['chabo'] = soup.select_one('.product_info_content .chabo dd').get_text()

    #음료명, 음료 코드, 음료 사진 url 정보
    drink_info['name'] = prod[0]
    drink_info['code'] = code
    drink_info['img_url'] = prod[2]
    db.starbucks.insert_one(drink_info)

    time.sleep(3)



dr.quit()
