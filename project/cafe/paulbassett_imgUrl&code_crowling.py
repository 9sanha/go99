
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 커피 고유 코드 크롤링 할 때 쓰는 코드
coffeeCode=[]
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#url 끝 : A => 커피, B => 논커피 음료
url = 'https://www.baristapaulbassett.co.kr/menu/List.pb?cid1=A'
#url = 'https://www.baristapaulbassett.co.kr/menu/List.pb?cid1=B'


data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#container > div.menuList > ul > li')
#container > div.menuList > ul > li:nth-child(1) > a > div.thum > img
#container > div.menuList > ul > li:nth-child(3) > a > div.thum > img
a=1
drink_info = []
img_url=[]
for tr in trs:
    t = ':nth-child(' + str(a) + ') > a'
    img_url.append('https://www.baristapaulbassett.co.kr/'+tr.select_one(t+'> div.thum > img')['src'])
    drink_info.append(tr.select_one(t)['onclick'])
    coffeeCode.append(str(drink_info[a-1]).split("'")[1].split("'")[0])
    a+=1

print(coffeeCode)
print(img_url)

#결과
coffeeCode=['PB180636', 'PB180640', 'PB170134', 'PB170054', 'PB179549', 'PB179548', 'PB170055', 'PB170065', 'PB170060', 'PB180596', 'PB180594', 'PB170157', 'PB170080', 'PB179437', 'PB170083', 'PB179737', 'PB179700', 'PB179699', 'PB179761', 'PB179759', 'PB179898', 'PB179376', 'PB179371', 'PB180498', 'PB180497', 'PB180524', 'PB179573', 'PB179575', 'PB179988', 'PB179826', 'PB179825', 'PB179343', 'PB179341']
nonCoffeeCode=['PB180643', 'PB180635', 'PB180638', 'PB179926', 'PB179763', 'PB179764', 'PB179765', 'PB179767', 'PB179768', 'PB180592', 'PB180495', 'PB180496', 'PB179874', 'PB179876', 'PB179230', 'PB179232', 'PB179956', 'PB180610', 'PB180612', 'PB180613', 'PB180611', 'PB179320', 'PB179203', 'PB179981', 'PB179736', 'PB179572', 'PB179696', 'PB179158', 'PB179163', 'PB179159', 'PB179164', 'PB179162', 'PB179192', 'PB179161', 'PB179191', 'PB179878', 'PB179880', 'PB179882', 'PB179884', 'PB179414', 'PB179415']
nonCoffee_imgUrl=['https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202106250849356511.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202106250856499561.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202107281157062280.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202003090144227051.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_2_201905081055325481.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201905081040557511.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201905081042462191.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201905081046442241.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201905300346425631.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202103030921175380.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202011050352546180.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202011050352076930.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201911201154098521.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201911200957167281.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210556246751.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_2_201904120720348180.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202004281115053170.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202104260852504110.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202105281111508511.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_2_202105280540471731.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202104260851176460.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210626327311.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210627458181.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_202006180853040050.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210628342191.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_2_202106240957057131.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210128273811.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210115358961.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903211143306621.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210117344521.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903211145428441.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210119093081.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903211150536601.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201904121034216800.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210113109981.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201911201001439141.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201911201000410161.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201911200959267741.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201911200958226391.png', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_2_201903210633483561.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/B/thumbnail_1_201903210631243151.jpg']
Coffee_imgUrl=['https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202107281159011570.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202107281159311510.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211036218861.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211031182001.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211042263731.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211033328911.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211021531581.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201912111105461651.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_2_201903250641135980.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202103031031363601.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202103031027429111.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211107237211.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211053056601.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211048508581.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903270305046650.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201904110903483990.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211117123241.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201904110901351460.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201905071253365671.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201905071251332911.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202004211059081041.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211105284401.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211056181001.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202011050351162550.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202011050351342170.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202101050430254591.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211113523011.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201903211115239201.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_202007211148507841.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201907050624303670.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_2_201907050625320680.jpg', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201904110903143820.png', 'https://www.baristapaulbassett.co.kr//upload/product/A/thumbnail_1_201904110902187290.png']
