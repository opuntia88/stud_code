#7.랜덤.
#랜덤은 '특정 범위내의 무작위값', '입력된 항목내의 범위내에서 무작위 선택'
#사용시 import random을 해서 라이브러리를 임포트하여야한다.

import random #random 함수를 사용하기위해 꼭 사용해야함.

n1 = random.random() #0과 1사이의 임의의 부동소수점의 수를 생성해서 n1에 저장.  ☞ 임의의 범주의 랜덤
n1= n1 * 100 #100을 곱하여 자연수로 만듬.
print("random 0~100->",n1)

n2=random.randint(0, 9) #0과 9까지(포함)사이의 임의의 정수를 선택.
print("random 0~9->",n2)

n3=random.randint(0, 1000)
n4=random.randint(0, 1000)
newrand= n3 / n4 #랜덤의 두수를 나눈 임의의 부동소수점 수를 생성.
print("newrand~->",newrand)

n5=random.randrange(0, 100, 5) #0부터 100까지 5의 배수중의 랜덤값
print("random ~ 5 multiple between 0 to 100 ->", n5)

colour = random.choice(["red", "black", "green"])#입력한 문자열들 중 하나를 임의로 선택해 뱐수에 저장
                                                 #문자열은 따옴으로 감싸지만 숫자는 그럴필요 없음.
print(colour)

