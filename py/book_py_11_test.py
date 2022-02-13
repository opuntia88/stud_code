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
inp03=array('i',[])
n=0
c=0#invalid literal for int() with base 10: '' -> c가 정수인지 값이 지정되지 않았으므로 28열에서 오류가 발생.
while n<5:
    c=int(input("enter the number between 10 to 20:"))
    if c<=20 and c>=10:
        inp03.append(c)
        n=n+1
    else:#10<=c<=20에 포함되지 않을 경우.
        print("outside the range")

for i in range(0,5):#하나의 항목씩 출력.
    print(inp03[i])


#91. 다섯개의 숫자를 담고있는 배열을 생성. 사용자ㅔ게 배열 전체를 출력 후 하나를 고르라고하여 리스트에 몇개가 있는지 출력.
inp04=array('i',[45,12,9,12,45])
n=0
print("the list is",inp04)
d=int(input("choose one number in array:"))
for i in inp04:
    if i == d:
        n=n+1#어레이 안에 있는만큼 더하기

print(d,"is ",n,"in array")

#92.두개의 빈 배열을 생성, 하나에는 사용자가 입력한 숫자를 세개를 넣고 다른하나에는 임의의 5개의 숫자를 담을것.
#   두개의 배열을 하나의 배열로 결합, 결합한 배열을 정렬하여 하나씩 출력.

inp05=array('i',[])#사용자 입력 어레이
for i in range(0,3):
    e=int(input("enter the neutral number:"))
    inp05.append(e)

ran05=array('i',[]) #임의의 정수 어레이
for i in range(0,5):
    g=random.randint(0,100)#임의로 생성된 정수를 생성.
    ran05.append(g)

inp05.extend(ran05)
inp05=sorted(inp05)
for x in inp05:
    print(inp05)


