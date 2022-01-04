#3. 문자열(string)
#특정 기호를 파이썬문자로 출력시, "->\" // '->\' // \->\\
#입력받을시, int로 묶으면 정수값, str로 묶으면 문자값으로 하는것.
#여러줄에걸쳐 문자열을 입력할 시, \n을 사용하거나 """으로 묶으면 된다.
#예제
inp1=input("enter the word:")
in1=int(len(inp1)) # 입력받은 이름의 변수의 길이를 찾는다.
print(in1)

inp2=input("enter the any word(could mix upper and lower word):")
in2=inp2.upper()#입력받은 문자를 대문자화시킬것
print(in2)

inp3=input("enter the word:")
print(inp3.capitalize()) #입력받은 문자의 첫글자만 대문자로 바꾸고 나머지는 소문자.

inp4=input("enter the word:")
in4=inp4.lower() #입력받은 문자를 소문자화 한다
print(in4)

inp5, inp6=input("enter the first name, last name(seperate):").split()
name=inp5+inp6 #입력받은 이름과 성을 결합한다.
print(name)

inp7=input("enter the some words:")
in7=inp7.title()#입력받은 모든 문자의 첫자를 대문자로 바꾸고 나머지를 소문자로 한다
print(in7)

inp8=input("enter the sentence:")
print(inp8.strip())#문자열의 시작과 끝에 있는 문자(또는 공백)을 제거한다.

print("paoapa sopa dupa"[5:11])#각 문자로 리스트로 만들어 5~11번째 단어를 출력

#failed to push some refs to 'https://github.com/opuntia88/stud_code.git'
#에러발생: git push -f origin//강제로 진행한다는 것이라
#가장 좋은건 pull->merge->push하는 것.