#35. 사용자의 이름을 입력받아서, 그 이름을 세번 출력하라.
nm1=input("enter your name:") 
for i in range(0,3):#0부터 3까지.
    print(nm1)

#36. 35번 프로그램을 수정하여 이름과 숫자를 입력받아서, 한줄에 하나씩 출력하라

nm2=input("enter the number:")
for i in range(0,3):
    print("%d \n %d"%(nm1,nm2))

#37. 사용자의 이름을 출력받아서 각 문자의 단어를 한줄에 하나씩 출력
nm3=input("enter your name:")
for i in nm3:
    print(i)

#38. 37번 프로그램을 수정하여 숫자도 입력하게 해서 각 문자를 입력한 숫자만큼 반복

nm4=input("enter the number:")

for i in nm3 (0,nm4):
    print(i)

#39. 1부터 12사이의 값을 입력하도록 요구하여, 해당숫자의 12까지의 곱셈표를 출력하라.
nm5=int(input("enter the number is between 1 tot 12:"))

for i in range(0,12):
    nm6=i*nm5
    print("%dx%d=%d"%(nm5,i,nm6))