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
    if n2>comp1:  # 컴퓨터의 값보다 사용자가 입력한 값이 큰 경우.
        print("too high")
    else:
        print("too low") #작은경우
    n2=int(input("enter the number betwwen 1~5:"))

    if n2==comp1: #위에서 입력된 n2의 값이 컴퓨터값과 동일 여부에 따라 판별하기위해 안쪽으로 들여넣기함.
        print("correct!")
    else:
        print("you lose.., answer is", comp1)

#56.1~10사이의 값을 선택, 사용자에게 숫자를 입력하도록해서 해당값을 맞출때까지 반복한다.
comp2=random.randint(1,10)
n3=int(input("match the number:"))
while comp2!=n3:#정답이 나올때까지 반복
    n3=int(input("incorrect!! please enter number again:"))
print("you matched!! congraturation~")

#57.56번의 값을 데려와서 입력한 숫자가 작은지 큰지를 알려주고 숫자를 다시 고르게 하라.
comp2=random.randint(1,10)
n3=int(input("match the number:"))
while comp2!=n3:
    if comp2>n3:# 컴퓨터 값보다 큰지 작은지 여부를 출력.
        print("Too low~")
    else:
        print("Too high~")
    n3=int(input("please enter number again:"))
print("you matched!! congraturation~")

#58. 임의로 생성된 두 정수를 덧셈식을 다섯개를출제하여, 사용자에게 맞추도록 한다. 그런 후 몇개를 맞추었는지 출력.
j=0
for i in range(0,5):#5문제만큼만 출력
    comp3= random.randint(1,100)
    comp4= random.randint(1,100)
    ans=comp3+comp4
    print(comp3,"+",comp4)
    n4=int(input("="))
    if n4 == ans:
        j=j+1
print("you corrected",j,"answers")   

#59. 다섯개의 색을 제시한 뒤 컴퓨터가 제시한 색상과 맞을경우 well done을 출력, 아닐경우 아래의 문장으러 위츠하게 표현한 후 맞출떄까지 반복.
#The decision came out of the blue. The new trainees are still very green.They want me to conform, to be lily-white. efforts to expand the outreach to black voters. The rims of her eyes were red with crying.
comp4=random.choice(["blue","green","black","red","white"])
color=input("What color is computer choose?(blue/green/black/white/red):")
color=color.lower()#소문자로 변경.
while comp4!=color:#컬러가 맞지않을경우
    if comp4 == "blue":
        print("The decision came out of the blue")
    elif comp4 == "green":
        print("The new trainees are still very green")
    elif comp4 == "black":
        print("efforts to expand the outreach to black voters.")
    elif comp4 == "white":
        print("They want me to conform, to be lily-white.")
    elif comp4 == "red":
        print("The rims of her eyes were red with crying.")
    else:#이 외의 문자를입력하였을 경우,
        print("try again~")
    color = input("enter color again:")
print("well done!")

