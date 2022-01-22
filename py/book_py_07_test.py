#52.1~100까지의 임의의 정수 출력
import random #random 함수를 사용하기위해 꼭 사용해야함.

n1 = random.random() #0과 1사이의 임의의 부동소수점의 수를 생성해서 n1에 저장.  ☞ 임의의 범주의 랜덤
n1= (n1 * 100) #100을 곱하여 1 이상의 유리수로 만듬.
print("random 0~100->",int(n1)) #정수로 만들기 위해, int로 엮어줌
#n1=random.randint(1,100)으로 해도 임의의 정수 사잇값이 출력됨.

#53.다섯개의 과일이름의 목록에서 임의의 과일을 출력하라.
f=random.choice(["apple","banana", "watermelon","cherry","papaya"])
print("Do you like",f,"?")

#54. 컴퓨터랑 동전 앞뒤맞추기 게임
peop=input("you threw coin to the sky. In that case, is coin front or back?(f/b):")
comp=random.choice(["f","b"]) #choice를 쓸떄 문자열을 쓸경우 ([])로 감쌀것.
if peop==comp:
    print("You win")
else:
    print("bad luck. Your coin was",comp)#틀렸을경우, 컴퓨터가 정한 코인값을 출력.

#55.1과 5사이의 값을 요청, 입력값이 맞으면 well done, 틀리면 한번더 입력하도록해서 맞으면 correct,거기서 틀리면 you lose출력
n2=int(input("enter the number betwwen 1~5:"))
comp1=random.randint(1,5)# 1과 5사이의 값을 임의로 선정
if n2==comp1:
    print("well done!")
else:
    if n2>comp1:
        print("too high")
    else:
        print("too low")
    n2=int(input("enter the number betwwen 1~5:"))
    if n2==comp1:
        print("correct!")
    else:
        print("you lose..")
