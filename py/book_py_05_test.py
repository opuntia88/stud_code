#35. 사용자의 이름을 입력받아서, 그 이름을 세번 출력하라.
nm1=input("enter your name:") 
for i in range(0,3):#0부터 3까지.
    print(nm1)

#36. 35번 프로그램을 수정하여 이름과 숫자를 입력받아서, 한줄에 하나씩 출력하라

nm2=int(input("enter the number:"))
for i in range(0,3):
    print("%s \n %d"%(nm1,nm2))#문자열의 경우, str 즉 %s라고 둔다.

#37. 사용자의 이름을 출력받아서 각 문자의 단어를 한줄에 하나씩 출력
nm3=input("enter your name:")
for i in nm3:
    print(i)

#38. 37번 프로그램을 수정하여 숫자도 입력하게 해서 각 문자를 입력한 숫자만큼 반복

nm4=int(input("enter the number:"))

for i in range(0,nm4):#사용자가 입력한 수만큼 반복을
    for j in nm3:#입력한 이름의 단어를
        print(j)

#39. 1부터 12사이의 값을 입력하도록 요구하여, 해당숫자의 12까지의 곱셈표를 출력하라.
nm5=int(input("enter the number is between 1 tot 12:"))

for i in range(1,13):#곱셈은 1부터 시작, 12까지 나와야하므로 13으로 끝 값을 설정.
    nm6=i*nm5 #곱셉의 결과값을 먼저 구해서 다음 함수식을 간결하게 만듬.
    print("%dx%d=%d"%(nm5,i,nm6)) #입력값xi=곱셈값

