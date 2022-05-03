from array import*

#105.'numbers.txt'라는이름의 새로운 파일을 생성, 한줄에 쉼표로 구분된 다섯개의 숫자를 추가.
#   프로그램을 실행하고나서 이 프로그램이 저장된 위치에 해당파일이 생성되어있는지 확인.

file=open("Numbers.txt","w") #다음의 이름으로 쓰기파일을 생성
file.write("1,")#해당내용을 파일에 작성
file.write("2,")
file.write("4,")
file.write("8,")
file.write("16\n")
file.close()#작성된 파일을 닫아서 저장되도록함.

file=open("Numbers.txt","r")
print(file.read())
file.close()

#106.'Names.txt'라는 이르므이 파일을 생성, 다섯명의 이름을 추가, 실행한후 제대로 작동되는지 확인.
file=open("Names.txt","w")#쓰기파일로 파일을 염.
file.write("GA\n")
file.write("NA\n")
file.write("DA\n")
file.write("RA\n")
file.write("MA\n")
file.close()

#107.위의 파일을 열고 파이썬으로 표시하라.
file=open("Names.txt","r")#읽기파일로 파일을 염.
print(file.read())#읽는 상태로 문자를 파이썬으로 출력,
file.close()#열린 파일을 다시 닫아줌,

#108.Names.txt파일을 열어 사용자에게 새로운 파일을 입력하라고 요청하고 파일 끝에 추가하고 전체파일을 출력.
file=open("Names.txt","a")
nm=input("please enter your name?:")
file.write(nm)
file.close()

file=open("Names.txt","r")
print(file.read())
file.close()

#109.
print("1)Create a new file\n2)Display the file\n3)Add a new item to the file")
nf=int(input("Make a selection 1,2 or 3:"))#답이 정수값이 나오므로 int로 엮어준다.
if nf==1:
    file=open("Subject.txt","w")#1
    sj=input("please enter the subject name:")
    file.write(sj+"\n")
    file.close()
elif nf==2:
    file=open("Subject.txt","r")
    print(file.read())
    file.close()
elif nf==3:
    file=open("Subject.txt","a")
    nsj=input("please enter a new subject name:")
    file.write(nsj+"\n")
    file.close()

    file=open("Subject.txt","r")
    print(file.read())
    file.close()

#110.앞의 파일을 이용해 목록의 이름을 출력, 그리고 이름들 중 하나를 입력하라고 요청하고 그 이름을 제외한 나머지의 이름을 Name2.txt에 저장.
file=open("Names.txt","r")# 일단은 파일을 열어서 전체 리스트를 출력한다.
print(file.read())
file.close()
inp1=input("please choose the name in top list:")#이름을 입력 받는다.
rep=inp1+"\n"#한 줄마다 읽어야 하므로 단락을 나눈다.

file=open("Names.txt","r")
for row in file: #해당파일의 이름을 줄마다 읽을 경우
    if row!= rep:#해당 줄이 사용자가 입력한 단어와 다를 경우
        file=open("Names2.txt","a")#추가 형식으로 파일을 연다.
        wd=row #문제가 생길 수 있으므로 이름을 변경.
        file.write(wd)#파일에 해당 단어를 추가한다.
        file.close()
file.close()



