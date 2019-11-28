import random
from bs4 import BeautifulSoup 
import requests
import urllib
import os.path
import sys 

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
    # 단어 리스트
    do = input("   테스트하고 싶은 번호를 입력하세요 : ")

    if do == 'exit' :
        break 

    vocab = [] # 단어 리스트 : [영단어, 뜻]의 형태로 저장됨.
    base_url = "https://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query=" # 영어 사전 주소
    session = requests.session() # 영어 사전 주소에 리퀘스트 요청

    if os.path.isfile("C:\\Users\dahyun\Desktop\English/"+ do +"_complete.txt") : # 저장 경로에 파일 존재할 경우
        with open("C:\\Users\dahyun\Desktop\English/"+ do +"_complete.txt", mode = 'r') as f:
            while True:   
                line = f.readline()
                if not line:
                    break
                vocab.append(str(line).replace('\n',''))
        f.close()
        odd = [] 
        even = []
        for b in range(0,len(vocab)) :
            if b%2 == 0 :
                odd.append(vocab[b])
            else : 
                even.append(vocab[b])
        vocab = []
        for c in range(0,len(odd)) :
            vocab.append([odd[c],even[c]])

    else : # 존재하지 않을 경우
        with open("C:\\Users\dahyun\Desktop\English/"+ do + ".txt", mode = 'r') as f: 
            while True:  
                line = f.readline()
                if not line:
                    break
                vocab.append(str(line).replace('\n',''))
        f.close()

        #vocab = list(set(vocab)) # 리스트 중복 검사
        for g in range(0,len(vocab)) : # 중복 검사한 후 원소 리스트 형태로 변환
            vocab[g] = [vocab[g]]

        for k in range(0,len(vocab)) : 
            printProgress(int((100/len(vocab)*(k+1))), 100, 'Progress:', 'Complete', 1, 50) # 상태바
            res = session.get(base_url+vocab[k][0]) # 단어에 관련된 주소에 리퀘스트 요청
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            span = soup.findAll('span', attrs = {'class' : 'fnt_k05'}) # span의 class=fnt_k05의 데이터 요청
            span = str(span).split(',')[0][23:] # 가장 먼저 뜨는 뜻을 선택하고, span <class=fnt_k05> 짤라냄
            if '</span>' in span : # </span> 이 있다면 제거
                span = span[:-7]
            vocab[k].append(span) # vocab 리스트에 하나씩 추가
        
        new_text = open("C:\\Users\dahyun\Desktop\English/"+ do +"_complete.txt", 'w') # 새로운 텍스트 생성 : 쓰기 형태
        for m in vocab : 
            new_text.write('%s\n'%m[0]) # 홀수 줄에 영단어
            new_text.write('%s\n'%m[1]) # 짝수 줄에 한글 뜻 입력
        new_text.close()

    def test5(vocab) : # 객관식 문제 
        _2ndtry = []
        num = 2
        random.shuffle(vocab)
        for question in vocab : 
            print('='*100)
            print(question[1])
            choose = random.sample(vocab, 4) # vocab에 있는 리스트 중 4개를 무작위로 뽑는다
            while question in choose : # 뽑은 리스트가 정답과 중복된 데이터라면 다시 뽑는다
                    choose = random.sample(vocab, 4)
            answerindex = random.randint(0,4)
            choose.insert(answerindex, [question[0]]) # 무작위 위치에 정답 배치
            print('')
            for i in range(1,6) :
                print('   %d : '%i,choose[i-1][0])
            print('')
            answer = input(': ')
            if answer == question[0] or answer == str(answerindex+1):
                print('정답입니다!')
                print('='*100+'\n')
            else : 
                print("틀렸습니다.")
                print("정답은 " + question[0] + " 입니다.")
                print('='*100+'\n')
                _2ndtry.append(question)

        print('정답률은 %s'%(int((1-len(_2ndtry)/len(vocab))*100)),'% 입니다.',end='')
        if len(_2ndtry) != 0 :
            print(' 오답을 진행하도록 하겠습니다.\n')

        while len(_2ndtry) != 0 :
            random.shuffle(_2ndtry)
            for question in _2ndtry :
                print('='*100)
                print(question[1])
                choose = random.sample(vocab, 4)
                while question in choose :
                    choose = random.sample(vocab, 4)
                answerindex = random.randint(0,4)
                choose.insert(answerindex, [question[0]])
                print('')
                for i in range(1,6) :
                    print('   %d : '%i,choose[i-1][0])
                print('')
                answer = input(': ')
                if answer == question[0] or answer == str(answerindex+1) :
                    print('정답입니다!')
                    print('='*100+'\n')
                    _2ndtry.remove(question)
                else : 
                    print("틀렸습니다.")
                    print("정답은 " + question[0] + " 입니다.")
                    print('='*100+'\n')
            print('%d번째 오답을 마쳤습니다. 틀린 개수는 %d개입니다.'%(num, len(_2ndtry)))
            num += 1
            if len(_2ndtry) != 0 :
                print('%d번째 오답을 시작합니다.'%num)
            print('')

    def run(vocab) : # 주관식 문제
        _2ndtry = [] # 오답을 위한 리스트
        num = 2 # 회차 카운트
        random.shuffle(vocab) # 리스트 섞기
        for question in vocab : # vocab 리스트 하나씩 반복
            print('='*100)
            print('%s/%s'%(vocab.index(question)+1,len(vocab)))
            print('')
            print("   "+question[1])
            answer = input('   : ')
            if answer == question[0] : # 입력이 question과 같다면 정답처리 
                print('\n   정답입니다!\n')
                print('='*100+'\n')
            else : # 오답 처리
                print("\n   틀렸습니다.")
                print("   정답은 " + question[0] + " 입니다.\n")
                while 1 :
                    re = input("")
                    if re == question[0] :
                        break
                    else :
                        print("\n   틀렸습니다.")
                        print("   정답은 " + question[0] + " 입니다.\n")
                print('='*100+'\n')
                _2ndtry.append(question)

        print('   정답률은 %s'%(int((1-len(_2ndtry)/len(vocab))*100)),'% 입니다.',end='')
        if len(_2ndtry) != 0 : # _2ndtry 리스트의 길이가 0이 아니라면 오답 진행
            print('   오답을 진행하도록 하겠습니다.\n')

        while len(_2ndtry) != 0 : # _2ndtry 리스트의 길이가 0이면 종료
            random.shuffle(_2ndtry)
            right = []
            length = len(_2ndtry)
            for question in _2ndtry :
                print('='*100)
                print('%s/%s'%(_2ndtry.index(question)+1,length))
                print('')    
                print('   '+question[1])
                answer = input('   : ')
                if answer == question[0] :
                    print('\n   정답입니다!\n')
                    print('='*100+'\n')
                    right.append(question) # 정답이면 리스트의 원소 제거
                else : 
                    print("\n   틀렸습니다.")
                    print("   정답은 " + question[0] + " 입니다.\n")
                    while 1 :
                        re = input("")
                        if re == question[0] :
                            break
                        else :
                            print("\n   틀렸습니다.")
                            print("   정답은 " + question[0] + " 입니다.\n")
                    print('='*100+'\n')
            print('   %d번째 오답을 마쳤습니다. 틀린 개수는 %d개입니다.'%(num, len(_2ndtry)))
            num += 1
            for i in right :
                _2ndtry.remove(i)
            if len(_2ndtry) != 0 :
                print('   %d번째 오답을 시작합니다.'%num)
            print('')

    while 1 : # 무한 반복 
        status = input('\n   명령어를 입력하세요 : ')
        print('') 
        if status == 'test' :
            run(vocab)
            print('   재시작을 원하신다면 test를, 종료하실려면 end를 입력하세요.')
        elif status == 'test5' :
            test5(vocab)
            print('   재시작을 원하신다면 test5를, 종료하실려면 end를 입력하세요.')
        elif status == 'end' :
            break # 실행 종료
        elif status == 'study' :
            for l in vocab : 
                print('   '+l[0]+' : ', end='')
                print(l[1])
                while 1 : # 무한 반복
                    practice = input('\n   따라 작성해보세요 : ')
                    if practice == l[0] : # 일치하면 반복 해제
                        break
                    else : # 틀리면 반복
                        print('   다시 작성하세요.')
                print('')
            print('')
        elif status == 'help' :
            print('   test : 단어 퀴즈 시작 \nstudy : 단어 목록 \nend : 종료\n')
        else : 
            print('   잘못입력하셨습니다.')