import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb://agapao1:1998@15.164.163.148/', 27017)
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
Analpersonalities = soup.select('#main-app > main > div.type-group.analysts > div > a')
Diplpersonalities = soup.select('#main-app > main > div.type-group.diplomats > div > a')
Sentpersonalities = soup.select('#main-app > main > div.type-group.sentinels > div > a')
Explpersonalities = soup.select('#main-app > main > div.type-group.explorers > div > a')


for Analpersonality in Analpersonalities:
    name = Analpersonality.select_one('h4')
    mbti = Analpersonality.select_one('h5')
    explain = Analpersonality.select_one('div')
    if name is not None:
        Name = name.text
        Mbti = mbti.text
        Explain = explain.text
        doc = {
            'Name' : Name,
            'Mbti' : Mbti,
            'Explain' : Explain
        }
        db.mbti.insert_one(doc)

for Diplpersonality in Diplpersonalities:
    name = Diplpersonality.select_one('h4')
    mbti = Diplpersonality.select_one('h5')
    explain = Diplpersonality.select_one('div')
    if name is not None:
        Name = name.text
        Mbti = mbti.text
        Explain = explain.text
        doc = {
            'Name' : Name,
            'Mbti' : Mbti,
            'Explain' : Explain
        }
        db.mbti.insert_one(doc)

for Sentpersonality in Sentpersonalities:
    name = Sentpersonality.select_one('h4')
    mbti = Sentpersonality.select_one('h5')
    explain = Sentpersonality.select_one('div')
    if name is not None:
        Name = name.text
        Mbti = mbti.text
        Explain = explain.text
        doc = {
            'Name' : Name,
            'Mbti' : Mbti,
            'Explain' : Explain
        }
        db.mbti.insert_one(doc)'''

for i in range(100):
    
    
        
        doc = {
            'Me' : '',
            'My' : '',
            'Result' : ''
        }
        db.match.insert_one(doc)


