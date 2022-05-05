#14.csv파일 읽기와 쓰기.
#csv는 comma seperated values. 일반적으로는 스프레드 시트 또는 데이터베이스에서 가져오기 형식
#각 행은 식별가능한 열로 나뉘기 떄문에 단순한 텍스트 파일보다는 데이터를 제어하는데 유용
#w-> 새로운 파일을 만들고 그 파일에서 작성. 만일 동일한 이름이 있을경우 새로운 파일을 작성후 덮어씀
#x-> 새로운 파일을 만들고 그 파일에서 작성. 만일 동일한 이름이 있을경우 덮어쓰지않고 프로그램이 충돌함.
#r-> 읽기작업만을 위해 파일을 열기때문에 어떠한 변경도 할 수 없다.
#a-> 쓰기작업만을 위해 파일을 열며 파일 끝에 데이터를 추가하게된다.

import csv #파이썬이 csv라이브러리의 명령어를 사용할 수 있도록 프로그램 상단에 있어야함

file=open("Stars.csv","w")
newR="Brian,73,taurus\n"#저장할 데이터의 입력.
file.write(str(newR))#여기서 입력받은 것을 문자열로 인식
file.close()

file = open("Stara.csv","a")
name=input("enter name:")
age=input("enter age:")
star=input("enter star sign:")
newRecord=name+","+age+","+star+"\n"
file.write(str(newRecord))
file.close()

file=open("Stars.csv","r")
for row in file:
    print(row)


file = open("Stars.csv","r")
reader = csv.reader(file)
rows = list(reader)
print(rows[1])

file = open("Stars.csv","r")
search = input("enter the data you are searching for: ")
for row in file:
    if search in str(row):
        print(row)