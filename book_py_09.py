#9.tuple,list,dictionary
#tuple: 정의 후 저장된 내용의 변경이 안됨, 저장시 데이터가 무엇인지 명시해야함.
#list:데이터 모음을 실행되는 동안 변경이 가능한 변수의 이름으로 저장가능한 일반적인 방법,다양한 데이터타입의 저장이 가능
#dictionary: 데이터를 식별하는데 도움이 되는 인덱스 또는 정의할 수 있는 키를 줄수있는 방법, 이 인덱스는 데이터의 추가 삭제와 별개로 유지.

from turtle import color


f_tuple=("apple","banana", "orange","strawberry") #()로 엮으면 튜플로 저장~변경 불가능한 항목의 모음이다.
print(f_tuple)
print(f_tuple.index("banana")) #strawberry의 인덱스를 출력.
print(f_tuple[3])#4번쨰 상수 출력

n_list=["john","tim","jack"]
print(n_list)
del n_list[1]#1번쨰 변수를 삭제
print(n_list)
n_list.append(input("add the name:"))#사용자가 입략한 이름을 추가함  
print(n_list)
n_list.sort()#알파벳순으로 정렬
print(n_list)
#print(sorted(n_list))-> 원래 리스트의 순서를 바꾸진 않고 순서대로 출력 // 다른타입의 데이터가 저장되어 있을경우 작동 x

colours = {1:"red",2:"orange",3:"yellow"} #컬러라는 딕셔너리 생성, 인덱스:항목순으로 저장.
print(colours)
colours[2]="yellow" #인덱스가 2인 변수의 값을 변경
print(colours)

x=[154,634,876, 865, 253]
print(len(x)) #리스트의 길이 출력
print(x[1:4])#리스트의 1,2,3에 있는 리스트를 출력.
for i in x:
    print(i)

num=int(input("enter the number: "))
if num in x: #x에 있는 수일 경우.
    print(num, "is in the list")
else:
    print("Not in the list")

x.insert(2,420)#인덱스 2의 420를 추가, 다른건 밀린다.
print(x)
x.remove(876)#리스트의 항목을 삭제. (인덱스를 알지못해도 사용가능), 데이터의 인스턴트가 한개 이상일 경우 첫번째 인스턴스가 삭제됨.
print(x)
x.append(993)#리스트끝에 숫자를 추가
print(x)
