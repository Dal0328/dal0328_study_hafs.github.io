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
    url = input("Quizlet 주소를 입력하세요 : ")

    session = requests.session() 
    res = session.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    print('잠시만 기다려주세요.')
    span = list(soup.findAll('span', attrs = {'class' : 'TermText notranslate lang-en'}))
    for i in range(0,len(span)) :
        printProgress(int((100/len(span)*(i+1))), 100, 'Progress:', 'Complete', 1, 50)
        span[i] = str(span[i])[43:]
        if '</span>' in span[i] :
            span[i] = span[i][:-7]

    do = input("저장할 파일명을 입력하세요 : ")

    new_text = open("C:\\Users\dahyun\Desktop\English/"+ do +"_complete.txt", 'w') # 새로운 텍스트 생성 : 쓰기 형태
    for m in span : 
        new_text.write('%s\n'%m)
    new_text.close()

    commend = input('다운로드가 완료되었습니다. 종료하실려면 exit를 누르세요. 계속 하고 싶다면 아무 버튼이나 누르세요. : ')
    if commend == 'exit' :
        break
