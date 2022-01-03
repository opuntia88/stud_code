#12 두 숫자를 입력받아, 큰 숫자부터 출력하라
num1,num2=input("enter the two numbers(should be different, seperate " " )").split()
numA,numB=int(num1,num2)
if numA>numB:
    print("%d > %d" %(numA,numB))
else:
    print("%d > %d" %(numB,numA))

#13.사용자에게 20보다 작은 수를 입력받아, 입력받은 값이 20보다 같거나 크면"too high", 작으면 "thank you"출력
num3=input("enter the a number is smaller than 20: ")
if num3 == 20 or num3 >20:
    print("too high~")
else:
    print("Thank you!")

#14. 사용자에게 10과 20사이의 수를 입력받아 사잇값일 경우 감사를 표하고 아닐경우 오류 표시하기
num4=input("enter the a number between 20 to 10: ")
if num4 <= 20 and num4 >= 10:
    print("Thank you")
else:
    print("incorrect number")

#15 사용자에게 좋아하는 색상을 입력받고, red를 입력받을 경우 "i love red,too" 출력하거, 아닐경우 레드선호의 답하기
coL=input("what's your favorite colot?:")
coloR=str.lower(coL) #문자를 소문자로 바꾸는 함수
if coloR=="red":
    print("i like red too~")
else:
    print("i don't like that color, i prefer red.")

#16.날씨가 비가오는지 묻고, 그렇다면 바람이 부는지도 확인하여 사용자에게 우산을 챙기고 조심여부를 안내.
in1=input("today's weather is rainy?(y/n):")
in2=input("today's weather is windy?(y/n):")
an1,an2=str.lower(in1,in2)
if an1 =="yes":#비가 올경우
    if an2 =="yes":#비오는데 바람까지 불 경우
        print("it is too windy to use an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Have a good day!")