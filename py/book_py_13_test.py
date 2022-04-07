#105.'numbers.txt'라는이름의 새로운 파일을 생성, 한줄에 쉼표로 구분된 다섯개의 숫자를 추가.
#   프로그램을 실행하고나서 이 프로그램이 저장된 위치에 해당파일이 생성되어있는지 확인.

file=open("Numbers.txt","w") #다음의 이름으로 쓰기파일을 생성
file.write("1,")
file.write("2,")
file.write("4,")
file.write("8,")
file.write("16")
file.close()

file=open("Numbers.txt","r")
print(file.read())

