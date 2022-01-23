from ctypes.wintypes import RGB
from re import T
import turtle

scr=turtle.Screen()
scr.bgcolor("white")
turtle.shape("turtle")
turtle.shapesize(1)
turtle.pensize(2)

#64.다섯개의 꼭지점이 있는 별모양을 만들어라.
turtle.right(72)#점의 방향을 별의 디폴트값 방향으로 둠.
                #왜냐면 별 내부각(36) 절반만큼 꺾어야 선이 시작해서 별이 만들어지면 정 형태가 됨.
#turtle.pencolor("yellow")
turtle.color("magenta")#윤곽선과 도형 색 모두
turtle.begin_fill()
for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)#108도 안에 별 안쪽각 36도
turtle.end_fill()    

turtle.exitonclick()