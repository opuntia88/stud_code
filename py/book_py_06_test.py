#45.total=0, 값을 계속요구하면서 총 합이 50을 넘으면 루프를 멈춘다.
t1=0
n1=int(input("enter the number: "))
while t1<50:
    n1=int(input("enter the number(hint:up!!): "))
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
while ans1=="y":
    n3=int(input("enter the number:"))
    t3=t3+n3#사용자가 y를 눌렀으므로, 입력받은 값을 더함
    ans1=input("Do you want to add the number?(y/n):")#또 더하는 함수를 진행여부를 물어봄
print("the total is", t3) 

#48.사용자가 초대하고 싶은 사람의 이름을 요청, 초대문구를 출력하면서 숫자 카운트를 한다. 더이상 초대하고싶은 사람이 없을경우, 몇명이 참석하는 지 출력.
nm1=input("who are you invite the party?:")
print(nm1,"has now been invited.")
n4=1
ans2=input("do you want to invite more?(y/n)")
while ans2=="y":
    nm1=input("who are you invite the party?:")
    print(nm1,"has now been invited.")
    n4=n4+1
    ans2=input("do you want to invite more?(y/n)")
print("you invited " ,n4 ,"people.")


#49.compnum이라는 변수 50 생성, 사용자에게 숫자를 입력받아 compnum과의 동일여부 판단후 엽앤 다운을 알려두고 다시 맞춰봄. 맞으면 몇번쨰로 맞는지 알려줌
comp=50
count=0
n5=int(input("match the number!:"))
while n5!=comp:
    if n5>comp:
        print("too high!")
    else:
        print("too low~")
    count=count+1#횟수 계산
    n5=int(input("match the number!:"))
print("well done, you attempted ",count,"times")

#50.사용자에게 10-20사이 입력요청, 이하면 too low,이상이면 too high 출력하며 루프, 사이입력시 thank you 출력
n6=int(input("enter the number between 10 to 20:"))
while n6>=20 or n6<=10:
    if n6>=20:
        print("too high~")
    else:
        print("too low~")
print("thank you")

#51.사용자가 입력한 값을 변형시켜, 문제를 출력하며 풀도록 함
n7=int(input("enter the any number:"))
n8=n7*2+3#수의 랜덤화
print("There are",n8, "green bottles hanging on the wall, if 1 bottle should accidentally fall")
n9=int(input("How many green bottles will be hanging on the wall?:"))#문제 출력
while n9!=n8-1:
    n8=n8-1
    print("There are",n8, "green bottles hanging on the wall, if 1 bottle should accidentally fall")
    n9=int(input("How many green bottles will be hanging on the wall?:"))#n8이 한개 감소한 상태에서의 문제풀이
    