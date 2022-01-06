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

