#14.csv파일 읽기와 쓰기.
#csv는 comma seperated values. 일반적으로는 스프레드 시트 또는 데이터베이스에서 가져오기 형식
#각 행은 식별가능한 열로 나뉘기 떄문에 단순한 텍스트 파일보다는 데이터를 제어하는데 유용
#w-> 새로운 파일을 만들고 그 파일에서 작성. 만일 동일한 이름이 있을경우 새로운 파일을 작성후 덮어씀
#x-> 새로운 파일을 만들고 그 파일에서 작성. 만일 동일한 이름이 있을경우 덮어쓰지않고 프로그램이 충돌함.
#r-> 읽기작업만을 위해 파일을 열기때문에 어떠한 변경도 할 수 없다.
#a-> 쓰기작업만을 위해 파일을 열며 파일 끝에 데이터를 추가하게된다.

import csv #파이썬이 csv라이브러리의 명령어를 사용할 수 있도록 프로그램 상단에 있어야함

file=open("Stars.csv","w")
newR="Brian,73,taurus\n"#저장할 데이터의 입력.-> 예시
file.write(str(newR))#여기서 입력받은 것을 문자열로 인식
file.close()

file = open("Stars.csv","a") #추가형식으로 파일을 연다.
name=input("enter name:") #이름을 입력받음
age=input("enter age:")  #나이를 입력받음
star=input("enter star sign:")  #별의 별명을 입력받음
newRecord=name+","+age+","+star+"\n" #입력받은 데이터를 먼저 입력했던 방식대로 출력
file.write(str(newRecord)) #문장을 입력하므로->str로 묶어둘 것
file.close()

file=open("Stars.csv","r")#읽기형식으로 파일을 연다
for row in file:#줄마다 출력
    print(row)


file = open("Stars.csv","r")#읽기형식으로 파일을 연다
reader = csv.reader(file) #파일을 여는 방식 #2
rows = list(reader)
print(rows[1])#두번째 열에있는 파일을 연다.

file = open("Stars.csv","r")
search = input("enter the data you are searching for: ")
for row in file:
    if search in str(row):
        print(row)#원하는 영역의 라인을 출력