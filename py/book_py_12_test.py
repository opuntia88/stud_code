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




