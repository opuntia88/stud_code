import turtle

scr=turtle.Screen()
scr.bgcolor("white")
turtle.shape("turtle")
turtle.shapesize(1)
turtle.pensize(2)

#66.각 선색상을 다르게하여 팔각형을 그려라.

for i in range(0,8):
    
    if i==0:
        turtle.color("red")
    elif i==1:
        turtle.color("orange")
    elif i==2:
        turtle.color("yellow")
    elif i==3:
        turtle.color("green")
    elif i==4:
        turtle.color("blue")
    elif i==5:
        turtle.color("purple")
    elif i==6:
        turtle.color("magenta")
    elif i==7:
        turtle.color("black")

    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(100)
    turtle.end_fill()

turtle.exitonclick()