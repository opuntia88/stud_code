#80.사용자에게 이름을 입력하라고 요청. 입력된 이름의 길이를 출력. 그 후 성을 입력하라고 요청 후 성의 길이를 출력. 
#그 후 성과 이름 사이에 공백을 하나두어 저장한 길이를출력하고 그를 출력하라.
from platform import java_ver


fn=input("enter your first name?:")
print("your first name is",len(fn),"word.")#이름의 길이 출력.
ln=input("enter your last name?:")
print("your last name is",len(ln),"word.")#성의 길이 출력
nm=ln+" "+fn#풀네임 지정
print("Your name is",nm,",",len(nm),"words.")

#81. 가장 좋아하는 과목의 이름을 입력받고 각 문자뒤에 -를 붙여서 출력하라
sbj=input("What is the your favorite subject?:")#가장 좋아하는 과목출력
for letter in sbj:
    print(letter,end="-") # **** 각 문자를 출력하고나서 사이에 -를 출력.

#82.시 한 구절을 사용자에게 표시하고, 시작 인덱스와 마지막 인덱스를 입력하도록 해서 입력한 두 문자값 사이의 문자를 출력.
print("\n\"time is gold\"", "\tword:",len("time is gold")-1)
sp=int(input("choose the start point between 0-12:"))
ep=int(input("choose the end point between 0-12:"))

if sp<ep:
    sp=sp
    ep=ep
elif sp>ep:
    sp=10-sp#sp가 끝나는 점보다 크므로     
else:
    ep+1
print("time is gold"[sp:ep])
#TypeError: cannot unpack non-iterable int object--> 별도의 식으로 정의해야함.

#83. 사용자에게 대문자로 문자를 입력하도록하여, 메세지에 소문자가 있다면 모두 대문자로 입력할 때까지 무한 반복함.
eng1=input("enter the uppercase word!:")
i=0 #관련된 식이 없을경우 장치를 만들면 됨, 
while i==0:
    if eng1.isupper():
        i=1
        print("yes! it is upper class")
    else:
        i=0
        eng1=input("please enter the UPPER CLASS word!:")

#84.사용자에게 영어단어를 입력하도록 하여 첫 두 문자만 대문자로 출력하라
#
# eng2=input("enter the english word:")
eng2="AppLe"
eng2=eng2.lower()
f=eng2[0:2].upper()#capitalize는 첫문자만 대문자로 바꾸는 것.
d=eng2[2:]#마지막 인덱스를 모르므로 이렇게 비워둠
print(f,d)
#print(eng2[0:2].capitalize(),eng2[2:])

#85.사용자의 이름을 입력받은 뒤, 이름에 모음이 몇개인지출력하라.
#nm1=input("enter your name!:")
nm1="choieunjeong"
vw=["a","e","i","o","u","w","y"]
j=0
for i in range(0,len(nm1)):
    if nm1[i] in vw: #여기서 앞의 변수는 무조건 변수여야함. 리스트나 튜블이 있어서는 오류가 남.
        j=j+1
print("the number of vowel is ", j)

#86. 사용자에게 새로운 비밀번호 입력을 요청, 비밀번호를 입력을 한번 더 요구한다, 맞으면 THANKYOU 
#    대소문자가 안맞으면  they must be in the same case라고 출력, 일치하지않으면 incorrect.
pw=input("enter the new password:")#패스워드 입력
ent=input("then, enter your password:")#패스워드입력,
if pw==ent:
    print("Thnakyou.")
elif pw.lower()==ent.lower()
    print("they must be in the same case.!")
else:
    print("incoreect")
#if pw!=ent:
#    ent=input("Again, enter your password:")#패스워드 재입력
#    if pw.isupper():
#        k=1
#    else:
#        k=0
#
#    if ent.isupper():
#        o=1
#    else:
#        o=0
#    ent=ent.lower()
#    pw=pw.lower()
#    if pw==ent:
#        if k==o:
#            print("incorrect!")
#        else:
#            print("they must be in the same case.") 
#    else: 
#        print("incorrect!") 
#
#print("thank you!!")