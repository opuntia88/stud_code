#파이썬은 대소문자에 민감
jack = 0  #변수의 초기화, 값설정
i, k, j = 10, 11, 12
jack = i+k
print(jack) #10+11의 값을 프린트
jack = j-i
print(jack) #12-10의 값을 프린트
jack = jack * 2
print(jack) #(12-10)*2의 값을 프린트
jack = k/jack
print(jack) #11를 (12-10)*2로 나누어 남은 나머지의 값을 프린트
jack = j//jack 
print(jack) #12를 3으로 나누어 남은 몫을 프린트

print("what is your age?") # 너의 나이는 얼마고
textvalue = int(input("enter the age /10: ")) #내 나이의 일의 자리 숫자 입력
numvalue = int(input("enter the number//10 : ")) #내 나이의 십의 자리 숫자 입력 
jack = (numvalue*10)+textvalue #내 나이 계산
print("my age is", jack) #한걸 출력




