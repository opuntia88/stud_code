#파티에 몇명을 초대하고싶은지 묻고, 10미만이면 이름을 묻고 "[이름]has been invited"을 입력한 숫자만큼 반복. 10 이상이면 "too many people을 출력"
n7=int(input("How many do you invite the people?:"))
if n7<10:
    for i in range(0, n7):
        nm6=input("enter your name:")
        print("%s has been invited" %nm6)
else:
    print("Too much people~")
