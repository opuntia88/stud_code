import math

#27.사용자에게 소수점이하 자릿수가 많은 숫자를 입력하게 요청. 이 숫자에 2를 곱한 결과를 출력한다.
nm1=float(input("enter the number of decimal places or more:"))#
Nm1=nm1**2 #2거듭제곱하기
print(Nm1)

#28. 27번의 수를 소수점 둘째자리로 출력.
print(round(Nm1,2))#소수 둘째자리까지 출력.

#29.사용자에게 500이상의 정수르 입력하라고 요청. 입력받은 숫자의 제곱근을 소수점 둘째자리로 출력.
nm2=int(input("enter the number over 500:"))
Nm2=math.sqrt(nm2)#제곱근으로 만듬
print(round(Nm2,2))#만든 제곱근을 소수 둘째자리까지 출력

#30.파이의 값을 소수 다섯번째 자리까지 출력.
nm3=math.pi #파이의 값으로 변경
print(round(nm3,5))#소수 다섯번째자리까지 출력

#31.사용자에게 원의 반지름을 입력받아 원의 넓이를 계산하여 출력한다.
r1=int(input("enter the number of radius:"))
R1=(r1**2)*math.pi #원의 넓이를 계산
R1=float(round(R1,5))#원의 계산하여 소수점 5번쨰자리까지 출력
print(R1)

#32. 원기둥의 반지름과 깊이 입력받아 원기둥의 부피를 구하여 소수점 셋째자리까지 구한다.
r2, h=input("enter the number of redius and heigth:").split()
R2=int(r2)
H=int(h)
cy1=((R2**2)*math.pi)*H #원기둥의 부피=(r^2)*h
print(round(cy1,3))

#33. 사용자로 두 수를 입력받아서, A를B로 나눈후 몪과 나머지를 보기쉽게 표현하기
a, b =input("enter the  two numbers(a>b):").split()
A = int(a)
B = int(b)
q=A//B #몫
r=A%B #나머지
print("The division of A to B is %d and remaining %d"%(q,r))

#34. 사용자가 선택한 선택지에 알맞는 도형의 넓이를 구하는 함수식을 생성, 다른 것이 입력될경우 오류메세지
print("1) Square \n2) Triangle\n\n")
ans=int(input("enter the number: "))
if ans==1:
    r3=int(input("enter the number of radius:"))
    print("the wideness of circle is"(r3**2)*math.pi)
elif ans==2:
    r4, h=input("enter the radius and height:").split
    int(r4, h)
    print("the wideness of cylinder is"((r4**2)*math.pi)*h)
else:
    print("incorrect message.")


