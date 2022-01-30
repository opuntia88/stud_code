#69.다섯개의 나라의 이름을 튜플로 출력하고 사용자에게 해당 이름중 입력하도록해 해당나라의 인덱스를 출력
nm1=("korea","canada","usa","mexico","russia")
for i in range(0,5):
    print(nm1[i])
q1=input("enter the country name in tuple list:")
if q1 in nm1:
    print(nm1.index(q1))#원하는 이름의 인덱스를 출력.
else:
    print("it's wrong!")#잘못 입력되었을경우

#70. 사용자에게 숫자입력을 요청하고, 입력한 위치의 국가의 이름이 출력되는 기능을 앞의 문제에서 추가하라
q2=int(input("enter the number between 0 to 4:"))
if q2>5:
    print("it's wrong")
else:
    print(nm1[q2])#입력된 인덱스의 나라의 이름을 출력.

#71. 두개의 스포츠이름을 담고있는 리스트를 생성하라. 이들중 사용자가 좋아하지않는 과목을 묻고 그 과목을 리스트에서 삭제한뒤 리스트에서 다시 출력하라
nm2=["soccer","tennis"]#리스트 생성
print("which sport do you hate in", nm2)
q3=input(":")#input의경우 다른 형식의 출력이 어려우므로 이렇게 나누어서 출력.
if q3 in nm2:
    nm2.remove(q3)#리스트에서 해당항목을 제거
    print(nm2)
else:
    print("it's wrong")

#72.교과목 여섯개가 담긴 리스트를 생성하고 그중에서 싫어하는 과목을 삭제하고 재출력하라
nm3=["korean","math","sociality","science","english","music"]
print("which subject do you hate between this?->",nm3)
q4=input(":")

if q4 in nm3:
    nm3.remove(q4)#싫어하는 과목 삭제
    print(nm3)
else:
    print("It's wrong input.")

#73. 사용자에게 좋아하는 음식을 네개 입력을 요청하게해서 인덱스의 번호와 항목이 모두 출력되도록 딕셔너리를 출력,
#    제거하고 싶은 항목을 묻고 그것을 제거. 남은 딕셔터리 출력,
f_d={}#딕셔너리 생성
f1=input("enter the food yau are like:")
f_d[1]=f1
f2=input("enter the food yau are like:")
f_d[2]=f2
f3=input("enter the food yau are like:")
f_d[3]=f3
f4=input("enter the food yau are like:")
f_d[4]=f4
print(f_d)
q5=int(input("enter the food you want to delete in dictionary index"))#여기서 int로 묶으면 바로 인덱스 입력이됨.
if q5 in f_d:
    del f_d[q5] #딕셔너리는 이렇게 삭제! *****
    print(f_d)
else:
    print("it's wrong")

#74.열개의 색이 담긴 리스트를 생성. 0에서 4사이에서 시작해서 5에서 9사이에서의 끝숫자를 출력하여 사잇값의 색상을 출력하라.
col=["red","orange","yellow","lightgreen","green","skyblue","blue","indigoblue","purple","pink"]
n1=int(input("enter the number 0~4:"))
n2=int(input("enter the number 5~9:"))
print(col[n1:n2])#해당 인덱스로부터 입력한 인덱스까지 출력.

#75.세자리숫자 네개가 담긴 리스트를 생성, 각 항목을 한줄에 하나씩 출력해서 입력을 요청.매칭되면 해당 인덱스를 출력, 아닐경우 "That's not in the list"를 출력하라.
nm5=["123","234","345","456"]
for i in range(0,4):
    print(nm5[i])
q6=input("enter the three-figure number:") #""로 들어가 있을경우에는 문자열로 들어가 있는 것이므로 int 로는 엮지않는디.
if q6 in nm5:
    print(nm5.index(q6))
    #print(nm5.index[q6])->예시 print(f_tuple.index("banana"))
#TypeError: 'builtin_function_or_method' object is not subscriptable -> []연산자를 사용할 수 없는 객체에 이연산자를 사용해서 그럼.
else:
    print("That's not in the list")

#TypeError: 'set' object is not subscriptable -> 리스트는 []로 묶고, 딕셔너리나 set문은 {}

#76.사용자에게 파티에 초대할 이름 세명을 입력을 요청하고 리스트에 저장. 원하는 만큼 입력을 요청. 거부하면 몇명을 초대했는지 출력.
nam=[]#리스트 선언 -> 빈데이터므로 값이 없음
#nam=[0]*10 #0값이 들어있는 10개의 방을 잡는다.
nam=input("who do you want to invite for party 3 people(seperate " "").split()
q7=input("do you want to invite more?(y/n)")
while q7=="y":
    jack=input("who do you want to invite for party:")
    nam.append(jack)
    q7=input("do you want to invite more?(y/n):")
print("you invite ",len(nam),"number of member.")
#IndexError: list assignment index out of range -> 빈리스트인데 없는 인덱스를 찾아서 생기는 문제. append나 insert로 추가.

#77.76번 프로그램을 이용해서 초대할 사람들의 이름이 리스트에 모두 추가되면 전체명단을 출력.리스트중 이름을 하나 출력하라고함
print(nam)
q8=input("please choose the name in list:")
print(nam.index(q8))#q8의 인덱스를 출력
print("do you want to invite:",q8,"?")
q9=input("(y/n):")
if q9!="y":
    nam.remove(q8)
    print(nam)
else:
    print("let's party")

#78. 네개의 tv프로그램 타이틀의 리스트를 생성, 한줄씩 출력. 그러고 새로운 프로그램을 입력받아 원하는 위치에 넣고 재출력한다.
prog=["runningman","muhandojeon","sininwang","inthesoop"]
for i in range(0,4):
    print(prog[i])
inp=input("enter the new program name!:")
inpN=int(input("And where so you want to place the program name!:"))#넣고싶은 위치를 설정,
prog.insert(inpN,inp)#넣고싶은위치에 넣을 항목을 정함.
print(prog)

#79. nums라는 빈 리스트를 생성, 사용자에게 숫자를 입력할 것을 요청. 
num=[0]*3
for i in range(0,3):
    num[i]=int(input("enter the number:"))
q10=input("do you want to add third number to list?:")
if q10 =="n":
    num.remove(num[2])
    print(num)
else:
    print(num)