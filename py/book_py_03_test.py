#20.사용자에게 이름을 입력받아 그것의 길이를 출력
nm=input("enter your name:")
num1=len(nm)#여기서 꼭 int로 씌워줄필요가 없음. 이미 len이 숫자의 값으로 만드는 함수이기 때문
print(num1)

#21. 사용자에게 이름을 입력받아 그 다음으로 성을 묻고, 이름과 성간에 공백하나를 두고 출력 및 
#    공백을 포함한 총 길이를 출력
fn, ln=input("enter you first name, last name(seperate to " "):").split()
fuN=ln+' '+fn #성과 이름사이에 띄어쓰기를 한 문자열을 저장
fN=len(fuN)
print(fuN,fN)

#22. 사용자에게 이름과 성을 소문자로 입력받아 각 문자의 첫글자만 대문자로 변경, 
#    성과 이름사이에 공백을 두어 결합, 그 결과 출력.
f1, l1=input("enter the firstname,lastname in lower words:").split()
F1= (f1).capitalize()#이건 각자 대문자화 해야함.
L1= (l1).capitalize()
print(L1+" "+F1)

#23. 사용자가 입력한 자장가를 사용자가 지정한 영역만큼만 출력하기
sn=input("enter the part of sleeping song:")
snum=len(sn)-1
print(snum)
n1, n2=int(input("enter the two numbers between 0 to %d :", snum))
if n1>n2:
    n4=n1,n3=n2
elif n1<n2:
    n4=n2,n3=n1
else:
    n4=n2, n3=n1
print(sn[n3:n4])

#24
w1=input("enter any word")
wo1=w1.lower()
print(wo1)