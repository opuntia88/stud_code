#45.total=0, 값을 계속요구하면서 총 합이 50을 넘으면 루프를 멈춘다.
t1=0
while t1<50:
    n1=int(input("enter the number: "))
    t1=t1+n1
print("total is", t1)

#46.숫자입력을 요청받아,입력값이 5를 넘을때까지 숫자를 요청.넘으면 "The last number you enterd is ~"출력하고 루프 종료
t2=0
t2=int(input("enter the any number:"))
while t2<5:
    t2=int(input("enter the any number:"))
print("The last number you entered is ", t2)#입력된 값이 5를 넘을 경우 출력

#47.사용자에게 숫자를 입력하라고 요청한 다음에 다음 숫자를 입력을 요구, 더 입력여부를 y/n로 묻고 반복루프후 y가 아닌 다른 답이 나온경우 루프 종료후 총합을 출력.
n2= int(input("enter the number:"))
n3= int(input("enter the number:"))
t3=n2+n3
ans1=input("Do you want to add the number?(y/n):")
ans1.lower()
while ans1!="y":
    n3=int(input("enter the number:"))
    t3=t3+n3#사용자가 y를 눌렀으므로, 입력받은 값을 더함
    ans1=input("Do you want to add the number?(y/n):")#또 더하는 함수를 진행여부를 물어봄
print("the total is", t3) 

#48.

