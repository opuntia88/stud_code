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

#73. 사용자에게 좋아하는 음식을 네개 요청하게해서 인덱스의 번호와 항목이 모두 출력되도록 딕셔너리를 출력,
#    제거하고 싶은 항목을 묻고 그것을 제거. 남은 딕셔터리 출력,
nm4={1:"pizza",2:"tart",3:"coffee",4:"bagel"}
print(nm4)
q5=input("what do you want to delete food i dictionary?")
if q5 in nm4:
    nm4.remove(q5)
else:
    print("it's wrong")