#35. 사용자의 이름을 입력받아서, 그 이름을 세번 출력하라.
nm1=input("enter your name:") 
for i in range(0,3):#0부터 3까지.
    print(nm1)

#36. 35번 프로그램을 수정하여 이름과 숫자를 입력받아서, 한줄에 하나씩 출력하라

n1=int(input("enter the number:"))
for i in range(0,3):
    print("%s \n %d"%(nm1,n1))#문자열의 경우, str 즉 %s라고 둔다.

#37. 사용자의 이름을 출력받아서 각 문자의 단어를 한줄에 하나씩 출력
nm2=input("enter your name:")
for i in nm2:
    print(i)

#38. 37번 프로그램을 수정하여 숫자도 입력하게 해서 각 문자를 입력한 숫자만큼 반복

n2=int(input("enter the number:"))

for i in range(0,n2):#사용자가 입력한 수만큼 반복을
    for j in nm2:#입력한 이름의 단어를
        print(j)

#39. 1부터 12사이의 값을 입력하도록 요구하여, 해당숫자의 12까지의 곱셈표를 출력하라.
nm3=int(input("enter the number is between 1 tot 12:"))

for i in range(1,13):#곱셈은 1부터 시작, 12까지 나와야하므로 13으로 끝 값을 설정.
    n3=i*nm3 #곱셉의 결과값을 먼저 구해서 다음 함수식을 간결하게 만듬.
    print("%dx%d=%d"%(nm3,i,n3)) #입력값xi=곱셈값

#40.50미만의 숫자를 입력하도록 요청, 50부터 입력한 숫자까지 카운트하여 입력된 숫자까지 출력한다.
nm4=int(input("enter the number under 50:"))
for i in range(0,51-nm4):#입력한 숫자까지 출력을 할 경우, 끝값에 1을 더해둔다.
    print(50-i)

#41. 이름과 숫자를 입력하도록 요청하여 입력한 숫자가 10미만이면 이름을 출력, 이상이면 too high를 출력.
n4,nm5=input("enter the number and name(seperate to " ":").split()
n4=int(n4)
#nm5=str(nm5)
if n4<=10:
    for i in range(0,n4):
        print(nm5)
else:
    print("Too High~")

#42.total=0, 5번 숫자입력을 요청하여 입력받은 숫자값을 더할지 여부를 묻고, 5번 물어본후 최후값을 출력.
