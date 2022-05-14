#111.다음의 csv파일을 book.csv 파일로 생성하시오
import csv

file=open("Books.csv","w")
file.write(" |   제목  |  저자  |  출간연도 |\n")#맨위에 각 형식을 잡아줌
for i in range(0,5):#5번 입력해야하므로 5번 반복.
    num=(str(i))#출력시 전부 문장화 시켜야하므로, str로 만들어줌.
    n=input("enter the book name:")
    w=input("enter the writer name:")
    d=input("enter the year of published:")
    l1=num+"_"+n+"|"+w+"|"+d+"\n"#하나의 문장으로 만들어줌
    file.write(str(l1))#해당 문장의 형식에 맞게 출력.
file.close()

file=open("Books.csv","r")#파일을 읽기형식으로 연다.
for row in file:
    print(row)#한 줄씩 출력.
file.close()

#112.위의 프로그램을 사용자에게 다른 내용의 이름을 요청해 각 행의 한줄에 하나씩 출력.
#file=list(csv.reader(open("Books.csv")))
#bk=[]
#for row in file:
#    bk.append(row)
#file=open("Book.csv","w")
c=1
for row in bk:
    inp=input("enter the another signal:") 
    l2=bk[c][0]+"|"+bk[c][1]+"|"+bk[c][2]+"|"+inp+"\n"
    file.write(l2)
    c=c+1
file.close()

#IndexError: list index out of range-> 지정되어있는 리스트의 값보다 큰 값의 리스트 데이터를 요구했을떄 발생하는 문제.

ile=open("Book.csv","r")#파일을 읽기형식으로 연다.
for row in file:
    print(row)#한 줄씩 출력.
file.close()