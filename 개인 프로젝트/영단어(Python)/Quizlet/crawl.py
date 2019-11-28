import random
from bs4 import BeautifulSoup 
import requests
import urllib
import os.path

def findWords(do):

    vocab = [] # 단어 리스트 : [영단어, 뜻]의 형태로 저장됨.
    base_url = "https://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query=" # 영어 사전 주소
    session = requests.session() # 영어 사전 주소에 리퀘스트 요청

    if os.path.isfile("C:/Users/dahyun/Desktop/Quizlet/Words/"+do +"_complete.txt") : # 저장 경로에 파일 존재할 경우
        return "이미 스크롤링을 시도한 파일입니다."
    else : # 존재하지 않을 경우
        with open("C:/Users/dahyun/Desktop/Quizlet/Words/"+ do + ".txt", mode = 'r') as f: 
            while True:  
                line = f.readline()
                if not line:
                    break
                vocab.append(str(line).replace('\n',''))
        f.close()

        vocab = list(set(vocab)) # 리스트 중복 검사
        for g in range(0,len(vocab)) : # 중복 검사한 후 원소 리스트 형태로 변환
            vocab[g] = [vocab[g]]

        for k in range(0,len(vocab)) : 
            res = session.get(base_url+vocab[k][0]) # 단어에 관련된 주소에 리퀘스트 요청
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            span = soup.findAll('span', attrs = {'class' : 'fnt_k05'}) # span의 class=fnt_k05의 데이터 요청
            span = str(span).split(',')[0][23:] # 가장 먼저 뜨는 뜻을 선택하고, span <class=fnt_k05> 짤라냄
            if '</span>' in span : # </span> 이 있다면 제거
                span = span[:-7]
            vocab[k].append(span) # vocab 리스트에 하나씩 추가
        
        new_text = open("C:/Users/dahyun/Desktop/Quizlet/Words/"+ do +"_complete.txt", 'w') # 새로운 텍스트 생성 : 쓰기 형태
        for m in vocab : 
            new_text.write('%s,'%m[0]) # 홀수 줄에 영단어
            new_text.write('%s\n'%m[1]) # 짝수 줄에 한글 뜻 입력
        new_text.close()
        return "완료되었습니다."