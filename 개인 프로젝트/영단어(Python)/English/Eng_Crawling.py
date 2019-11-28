from bs4 import BeautifulSoup 
import requests
import urllib
import sys
import os.path

# 소스 출처 :  https://yujuwon.tistory.com/entry/python%EC%97%90%EC%84%9C-Progressbar-%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100): 
    formatStr = "{0:." + str(decimals) + "f}" 
    percent = formatStr.format(100 * (iteration / float(total))) 
    filledLength = int(round(barLength * iteration / float(total))) 
    bar = '#' * filledLength + '-' * (barLength - filledLength) 
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)), 
    if iteration == total: 
        sys.stdout.write('\n') 
    sys.stdout.flush() 

while 1 : 
    ver = input('사전 : dic, 웹스크롤링 : scrawling \n: ')
    if ver == 'dic' :
        while 1 :         
            eng = input("\n영어단어를 입력해주세요 : ")
            print('')

            base_url = 'https://www.synonym.com/synonyms/'
            try : 
                session = requests.session()
            except ValueError : 
                pass
            res = session.get(base_url+eng) # 단어에 관련된 주소에 리퀘스트 요청
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            span = list(soup.findAll('li', attrs = {'class' : 'syn'}))
            
            for i in range(0,len(span)) :
                printProgress(int((100/len(span)*(i+1))), 100, 'Progress:', 'Complete', 1, 50)
                span[i] = str(span[i])[36:]
                if '</li>' in str(span[i]) : # </span> 이 있다면 제거
                    span[i] = str(span[i])[:-6]
                if '</a>' in str(span[i]) : # </span> 이 있다면 제거
                    span[i] = str(span[i])[:-4]
                span[i] = list(set(list(span[i].split('">'))))[0]

            for k in span : 
                print(k, end=', ')
            print('')
    
    elif ver == 'dic_kor' :

        while 1 :         
            eng = input("\n영어단어를 입력해주세요 : ")
            print('')

            base_url = 'https://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query='
            try : 
                session = requests.session()
            except ValueError : 
                pass
            res = session.get(base_url+eng) # 단어에 관련된 주소에 리퀘스트 요청
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            span = list(soup.findAll('span', attrs = {'class' : 'fnt_k05'}))
            span = str(span).split(',')[0][23:] # 가장 먼저 뜨는 뜻을 선택하고, span <class=fnt_k05> 짤라냄
            if '</span>' in span : # </span> 이 있다면 제거
                span = span[:-7]

            print(span)
        
    elif ver == 'scrawling' :
        pass
    elif ver == 'exit' :
        break
    else :
        print('잘못 입력하셨습니다.')