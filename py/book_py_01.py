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

print("what is your age?")
textvalue = int(input("enter the age /10: "))
numvalue = int(input("enter the number//10 : "))
jack = (numvalue*10)+textvalue
print("my age is", jack)




