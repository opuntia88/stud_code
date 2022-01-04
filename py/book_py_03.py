#3. 문자열(string)
#특정 기호를 파이썬문자로 출력시, "->\" // '->\' // \->\\
#입력받을시, int로 묶으면 정수값, str로 묶으면 문자값으로 하는것.
#여러줄에걸쳐 문자열을 입력할 시, \n을 사용하거나 """으로 묶으면 된다.
#예제
inp1=input("enter the word:")
in1=int(len(inp1)) # 입력받은 이름의 변수의 길이를 찾는다.
print(in1)

inp2=input("enter the any word(could mix upper and lower word)")
in2=inp2.upper()#입력받은 문자를 대문자화시킬것
print(in2)

inp3=input("enter the word:")
print(inp3.capitalize()) #입력받은 문자의 첫글자만 대문자로 바꾸고 나머지는 소문자.

inp4=input("enter the word:")
in3=inp3.lower() #입력받은 문자를 소문자화 한다
print(in3)

inp5, inp6=input("enter the first name, last name(seperate):").split()
name=inp5+inp6 #입력받은 이름과 성을 결합한다.
print(name)

inp7=input("enter the some words:")
in7=inp7.title()#입력받은 모든 문자의 첫자를 대문자로 바꾸고 나머지를 소문자로 한다
print(in7)

inp8="Your name is Jack"
print(inp8.strip(" "))#문자열의 시작과 끝에 있는 문자(또는 공백)을 제거한다.

print("paoapa sopa dupa"[5:11])