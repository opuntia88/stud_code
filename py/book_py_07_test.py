#52.1~100까지의 임의의 정수 출력
import random #random 함수를 사용하기위해 꼭 사용해야함.

n1 = random.random() #0과 1사이의 임의의 부동소수점의 수를 생성해서 n1에 저장.  ☞ 임의의 범주의 랜덤
n1= (n1 * 100)//100 #100을 곱하여 자연수로 만듬.
print("random 0~100->",n1)
