prog=["runningman","muhandojeon","sininwang","inthesoop"]
for i in range(0,4):
    print(prog[i])
inp=input("enter the new program name!:")
inpN=int(input("And where so you want to place the program name!:"))#넣고싶은 위치를 설정,
prog.insert(inpN,inp)#넣고싶은위치에 넣을 항목을 정함.
print(prog)