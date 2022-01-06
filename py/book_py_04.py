import math
#4.수학함수
#수학함수의 경우, 데이터가 정수또는 부동소수점일경우에만 사용가능.

nm1=input("enter float number:")
print(round(nm1,2)) # ► 숫자를 반올림하여 소수점 둘째자리까지 표현한다.

nm2=input("enter a neutral number:")
print(nm2**3) #  ► A**B는 a의 b거듭제곱이다!
math.sqrt(nm2) # ► 숫자의 제곱근을 구함, 사용시 import math를 반드시 추가해야함

nm3=float(input("enter number:")) 
# ► 정수부분과 소수부분으로 나누어지는 소수점을 가진 수를 받는다.

m4=math.pi # ► 소수 15자리까지 파이의 값을 반환, 사용시 import math를 반드시 추가해야함
print(m4)

m5, m6=int(input("enter the two numbers(must a>b):"))
m7=m5//m6 # 몫 연산
m8=m5%m6 # 나머지 연산

