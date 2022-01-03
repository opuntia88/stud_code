#if문
#==: ~와 같다/ !=: ~와 같지않다/ >=: ~보다 크거나 같다/ <=: ~보다 작거나 같다
num=input("enter the  any number:")
if num >= 10:
    print("this is bigger than 9")
elif num == 9:
    print("this is 9")
else:
    print("this is smaller than 9")

#str.lower(text): 텍스트를 소문자로 바꾸는 함수
num=input("enter the number between 10 to 20:")
if num >= 10 and num <=20: #num이 10과 같거나 크고 20과 같거나 작을경우
    print("THAT'S RIGHT!")
else:
    print("OH,,,NO")

num=input("enter the number between 1 to 6:")
if num == 1 and num ==3: #num이 1과 같거나 3과 같을경우
    print("THAT'S RIGHT!")
else:
    print("OH,,,NO")