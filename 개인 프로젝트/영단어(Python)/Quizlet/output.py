from bs4 import BeautifulSoup 
import requests
import urllib
import os.path

def quizletCrawl(url):
    session = requests.session() 
    res = session.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    span = list(soup.findAll('span', attrs = {'class' : 'TermText notranslate lang-en'}))
    for i in range(0,len(span)) :
        span[i] = str(span[i])[43:]
        if '</span>' in span[i] :
            span[i] = span[i][:-7]
    new_text = open("Words/quizletcrawl.txt", 'w') # 새로운 텍스트 생성 : 쓰기 형태
    for m in range(0,len(span),2) : 
        new_text.write('%s,%s\n'%(span[m],span[m+1]))
    new_text.close()
    return "완료되었습니다."