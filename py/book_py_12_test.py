#96.다음 내용의 2차원 리스트로 생성하라.
l1=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
for i in l1:
    print(i)

#for i in a-> 는 리스트 a에서 요소를 꺼내서 i에 저장하고, 꺼낼 때마다 코드를 반복합니다. 
#           따라서 print로 i를 출력하면 모든 요소를 순서대로 출력할 수 있습니다.

#97. 사용자에게 행과 열을 선택하도록해서 위의 리스트에서 해당값을 출력.
r1=int(input("choose the row number between 0 to 3:"))
if 0<=r1<=3:
    c1=int(input("choose the column number between 0 to 2:"))#행의 범주가 맞을 경우
    if 0<=r1<=2:
        print("you choosed",l1[r1][c1])
    else:
        print("you entered wrong input")
else:
    print("you entered wrong input")

#98.위의 리스트에서 사용자에게 표시할 행을 요청하고 출력, 새로운 값을 요청하고 추가하야 다시 행을 출력하라.
r2=int(input("enter the number between 0 to 3:"))
print(l1[r2])
n2=int(input("enter the number for putting in the list:"))
l1[r2].append(n2)#원하는 행에 숫자를 추가한다.
for i in l1:
    print(i)

#99.요청받은위치의 행을 출력하여 그중 열의 위치를 입력받아 출력한다. 값을 변경의 원함여부를 요청해 그럴경우 변경해 행을 출력,
r3=int(input("choose the row number between 0 to 3:"))#원하는 행의 위치를 선택
print(l1[r3])
c3=int(input("choose the column number between 0 to 2:"))#원하는 열의 위치를 선택
print(l1[r3][c3])
ans3=input("do you want to change the data?(y/n):")#이 위치의 값을 변경할 건지 선택
if ans3=="y":#바꾸길 원할 경우
    cng=int(input("enter the number:"))
    l1[r3][c3]=cng
    print(l1)
else:
    print("you entered wrong word")

#100.2차원 딕셔너리를 사용하여 각 사람이 서로 다른 지역에서 만든 매출을 보여주는 다음의 데이터를 생성하다.
sales={"John":{"n":3056, "s":8463, "e":8441, "w":2694},"Tom":{"n":4832, "s":6786, "e":4737, "w":3612},
        "Anne":{"n":5239, "s":4802, "e":5820, "w":1859},"Fiona":{"n":3904, "s":3645, "e":8821, "w":2451}}

print(sales)

#101. 위의 프로그램을 사용해서 사용자에게 이름과 지역을 입력하라고 요청. 그와 관련된 데이터를 출력,
#       변경하려는 데이터의 이름과 지역을 입력받아 매출 수치를 변경, 해당이름의 모든지역의 매출을 출력.

r4=input("please choose the name:")#행선택
if r4 in sales:#행 선택 잘못입력한 경우
    print(sales[r4])
c4=input("choose the city:")#열선택
if c4 in sales[r4]:#열 선택 잘못입력한 이유
    print(sales[r4][c4])#선택한 위치의 매출을 출력
rev=int(input("enter the sales cost to change:"))#바꿀값을 출력
sales[r4][c4]=rev
print(sales[r4])#바꾸어 출력

#102.네명의 이름과 나이 신발사이즈를 입력하라고 요청. 입력된 이름중 하나를 입력하라고 요청한 뒤 입력된 이름의 나이와 신발사이즈를 출력한다.


market={}
for i in range(0,3):
    nm=input("enter the name:")#행의 이름을 입력받음
    ag=int(input("enter the age:"))
    sz=int(input("enter the shoe size:"))
    market[nm]={ag:sz}
print(market)

qst=input("choose the name")
if qst in market:
    print(market[qst])

#103. 102번 프로그럄을 수정해서 모든사람의 나이와 이름을 출력.
for i in range(0,3):
    nm=input("enter the name:")#행의 이름을 입력받음
    ag=int(input("enter the age:"))
    sz=int(input("enter the shoe size:"))
    market[nm]={ag:sz}
    print(nm,market(nm))