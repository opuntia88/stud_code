import turtle

scr=turtle.Screen()
scr.bgcolor("white")
turtle.shape("turtle")
turtle.shapesize(1)
turtle.pensize(2)

#67.패턴
turtle.penup()
#turtle.right(185)
#turtle.forward(50)
for i in range(0,10):
    turtle.left(4.5)#144=4.5*2+135, 외부의 점 이동을 위한 방향전환
    turtle.forward(100)
    turtle.right(40.5)#180-(135+4.5)=40.5
    turtle.pendown()#외부선을 제외한 도형만 선을 그림
    for j in range(0,8):
        turtle.right(45)#팔각형의 내부각
        turtle.forward(88)
    turtle.penup()

turtle.exitonclick()