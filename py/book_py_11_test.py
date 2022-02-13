from array import *
import random
import math

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

inp05.extend(ran05)#두개의 어레이를 결합
inp05=sorted(inp05)#정렬:오름차순으로 
for i in range(0,8):
    print(inp05[i])

#93.사용자에세 숫자 다섯개를 입력받아 정렬하고 표시, 배열의 숫자중 하나를 고르라고 사용자에게 요청
#   그리고 배열중 숫자를 하나 고르라고 하여 그 값으 배열에서 삭제하고 새로운 배열값을 저장.

inp06=array('i',[])
for i in range(0,5):
    f=int(input("enter the number:"))
    inp06.append(f)
inp06=sorted(inp06)#리스트에서 오름차순으로 정렬.
print("array is",inp06)
qst06=int(input("Choose the number in the list:"))
inp06.remove(qst06)#리스트에서 제거
print(inp06)

#94. 다섯개의 숫자들을 가진 배열을 출력, 숫자들중 하나들 사용자로 하여금 고르도록 하여 해당 인덱스를 출력.
#    숫자가 없을 경우 입력될떄까지 반복.
inp07=[32,25,23,22,11]
print(inp07)
qst07=int(input("choose the number in the array:"))
false=0
while false!=1:
    if qst07 in inp07:
        print(qst07,"is in the" , inp07.index(qst07))#인덱스를 출력
        false = 1#제대로 입력할 경우 출력
    else:
        qst07=int(input("No, try again. choose the number in the array:"))


#95. 소수점 이하의 두자리가 있는 10과 100사잉의 숫자 다섯개를 포함하는 배열 생성, 사용자에세 2와 5사이의 수를 입력받음
#    입력한 숫자가 범위에 없는 숫자일 경우 에러메세지를 출력, 맞을 경우 사용자가 입력한 숫자를 두자리 숫자까지 출력.

inp07=[12.34,23.45,34.56,45.67,67.89]
qst07=int(input("enter the number between 2 to 5: "))
false=0
ans=0
while false!=1:
    if qst07>=2 and qst07<=5:
        for i in range(0,5):
            ans=inp07[i]/qst07
            inp07[i]=round(ans,2)#사용자가 고른숫자로 소수를 나누어 소수점 2자리까지만 배열에 추가.
            false=1
            #inp07[i]=round(inp07[i],2)
    else:
        print("that's wrong.")
        qst07=int(input("enter the number between 2 to 5: "))
print(inp07)