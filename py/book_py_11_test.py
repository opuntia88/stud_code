from array import *
import random

#88. 다섯개의 정수를 입력받아 배열에 저장. 정렬한 뒤 역순으로 출력.
inp01=array('i',[])
for i in range(0,5):
    a=int(input("enter the neutral number:"))
    inp01.append(a)#inp01정렬에 하나씩 추가.

inp01=sorted(inp01) #오름차순으로 정렬
inp01.reverse()#역순으로 정렬
print(inp01)

#89.정수들을 저장할 배열을 생성, 임의의 수 다섯개를 생성하고 배열에 저장, 배열을 한줄에 하나씩 출력

inp02=array('i',[])
for i in range(0,5):
    b=random.randint(0,100)#임의의 정수를 생성
    inp02.append(b)#임의로 생성된 수를 배열에 추가.
    print(inp02[i])

#90.사용자에게 숫자를 입력하라고 요청한다. 10에서 20사이일 경우 배열에 저장, 다른값이면 outside the range출력
#   다섯개가 입력이 되면 thank you 출력하여 배열항목에 하나씩 출력.
