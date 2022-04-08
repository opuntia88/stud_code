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
