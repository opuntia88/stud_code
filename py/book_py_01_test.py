#import list

#01. 사용자의 이름을 입력받아서 다음과 같이 출력하라: hello [이름]
maname = input("enter your name") #입력된 e.y.n에 나의 이름을 입력한 변수를 저장한 뒤
print("hello", maname) #hello 뒤에 이름으로 저장된 변수를 출력

#02. 사용자의 이름을 입력받은 다음 사용자의 성을 입력받아서 다음과 같이 출력하라: hello [이름][성]
name1 = input("enter your first name: ") #이름을 입력받음
name2 = input("enter your last name: ") #성을 입력받음
print("hello", name1, name2) #다음과 같이 출력을 할 경우, 출력할 값을 순서대로 쉼표로 연결해줌

#03. "what do you call a bear with no teeth" 라는 농담을 치고나서  다음 줄에 " a gummy bear!"이라는 문장을 출력하기
print("What do you call a bear with no teeth?\nA gummy bear!")

#04. 사용자로 부터 2개의 숫자를 입력받아서 더한 결과를 다음과 같이 출력하라: the total is [결과]
intnum1, intnum2 = input("enter the any two numbers:").split()
#.split()은 공백을 기준으로 앞뒤의 문자열을 쪼개서 리스트로 만들어주는 함수.해당 함수는 각 변수를 문자로 인식.
#자세하게는 .split(sep, maxsplit)에서 sep이라는 기준(ex. 공백, 쉼표)을 중심으로 maxsplit의 값만큼 문자열을 쪼갠다.
no1=int(intnum1) #입력된 intnum1,2를 정수의 값으로 저장
no2=int(intnum2)
total1 = no1+no2 #그 합을 구함
print("the total is", total1)

#05.사용자로부터 3개의 숫자를 입력받는다. 첫번째와 두번째 숫자를 더한값에 세번째 값을 곱한결과를 다음과같이 출력하:the answer is[]
a,b,c=input("enter the three numbers(seperate to ,):").split(",") #이번에는 쉼표를 기준으로 각 문자를 쪼갠 리스트를 생성
num_a=int(a)
num_b=int(b)
num_c=int(c)
#ans=(num_a+num_b)*num_c
#print("the answer is",ans)
print("the answer is",(num_a+num_b)*num_c)#따로 더한값을 정의하지않고 출력창에 계산식을 올려 출력

#06. 사용자로 하여금 처음에 가진 피자조각수를 입력받고, 몇조각을 먹었는지 입력받아서 남은 조각수를 입력받아 사람에게 익숙한 형식으로 출력하라
firP=int(input("enter the number of slices of pizza at first:"))
eatP=int(input("enter the number of slices of pizza you ate: "))
leftP=firP-eatP
print("⍙\n"*leftP)

#07. 사용자로 부터 이름과 나이를 입력받아 다음과 같이 출략하시오: [이름] next birthday, you will be [나이]
a, b =input("enter your name and age(seperate to ,):").split(",") #원하는 값을 
nm=str(a)
bt=int(b)+1
print("%s! next birthday, you will be %d-year-old" %(nm, bt)) #같은 형식의 값을 출력하기위해서 다음과 같이 괄호로 묶는다

#08. 계산서의 총 가격과 몇명이 같이 식사했는지 입력받는다. 총 가격을 인원수로 나누고 사람씩 얼마를 내야하는지 출력하라
cost=[]  #cost를 리스트로 지정 
a = input("how much is the each prices of menu(seperate" ")").split()
b=int(a)
peop= input("how many does the number of people ate with you? (include you) ")
#for i in range(b):
    #al=sum
print("the number of guest: " %peop)
print("\nthe price to pay for food: " %sum(b))

#09. 사용자로부터 입력받은 시간이 각 단위별로 값이 얼마인지 환산하기
nw=input(" 원하는 값의 숫자를 입력하시오: ")
ti=int(nw)
mn=ti*60
sc=mn*60
print( "%d는 %d분과%d분과 같은 시간입니다" %(ti,mn,sc))
