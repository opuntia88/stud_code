#10. 다양한 문자열 처리.
#string: 계산작업이 필요없는 문자들의 그룹
#각 문자를 개별문자들로 인식할 수 있으며 각 문자를 인덱스로 식별가능

msg="STRINGCASE"
if msg.isupper():#대문자일 경우를 확인
    print("Uppercase")
else:
    print("Lowercase")

msg="stringtest"
if msg.islower():#소문자일 경우를 확인
    print("Lowercase")
else:
    print("Uppercase")

msg="Hello"
for letter in msg:#각 문자별로 출력
    print(letter,end="*")#각 문자 끝에 *를 출력.