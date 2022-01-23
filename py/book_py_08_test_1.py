import turtle

scr=turtle.Screen()
scr.bgcolor("yellow")
turtle.color("black","green")
turtle.shape("turtle")
turtle.shapesize(1)
turtle.pensize(2)

#60. 정사각형을 그려라.
n1=100
#int(input("enter the any number:"))
for i in range(0,4):
    turtle.forward(n1)
    turtle.right(90)

turtle.exitonclick()