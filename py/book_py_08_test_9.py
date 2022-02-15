import turtle
import random

scr=turtle.Screen()
scr.bgcolor("white")
turtle.shape("turtle")
turtle.shapesize(1)
turtle.pensize(2)

#67.랜덤함수를 이용해서 각 선의 길이, 개수, 회전 각도를 정하라.
turtle.penup()#초기값 설정을 위한 이동의 선이 보이지않도록 펜을 띄움
n_len=random.randint(12,100)#선의 길이=>
n_num=random.randint(4,20)#선의 갯수->내부 도형의 
n_ang=random.randint(20,180)#회전각도
turtle.color("green","")#속을 색칠하지않은 도형 윤곽선 채색

a=int(720//n_ang) #회전각도를 바탕으로 두바퀴를 돌도록 내부 도형의 갯수를 선정
aa=(180-(180*(a-2)//a)) #겉 선의 외부각을 계산
b=180-(180*(n_num-2)//n_num) #해당 내부도형의 외부각을 계산
for i in range(0,a):#외부의 형태를 잡기위한 회전.
    turtle.right(aa)
    turtle.forward(100)
    turtle.begin_fill()
    turtle.pendown()#내부 도형만 그림을 그림
    for j in range(0,n_num):#내부 도형 그리기
        turtle.right(b)#해당 선 도형이 정도형일 경우의 각도계산.
        turtle.forward(n_len)#원했던 랜덤 길이만큼
    turtle.penup()#선 이동을 위한 선 띄우기
    turtle.end_fill()

turtle.exitonclick()