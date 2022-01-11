#35. 사용자의 이름을 입력받아서, 그 이름을 세번 출력하라.
nm1=input("enter your name:") 
for i in range(0,3):#0부터 3까지.
    print(nm1)

#36. 35번 프로그램을 수정하여 이름과 숫자를 입력받아서, 한줄에 하나씩 출력하라

nm2=input("enter the number:")
for i in range(0,3):
    print("%d \n %d"%(nm1,nm2))

