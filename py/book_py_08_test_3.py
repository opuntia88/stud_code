import turtle

scr=turtle.Screen()
scr.bgcolor("yellow")
turtle.shape("turtle")
turtle.shapesize(1)
turtle.pensize(2)

#60. 정사각형을 그려라.
#n1=100
#int(input("enter the any number:"))
#for i in range(0,4):
#    turtle.forward(n1)
#    turtle.right(90)

#61.삼각형을 그려라
#for i in range(0,3):
#    turtle.forward(100)
#    turtle.right(120)



#62.원을 그려라.
#for i in range(0,360):
#    turtle.forward(1)
#    turtle.right(1)



#63. 서로 붙어있지않는 세게의 정 삼각형을 그려라, 세개의 정삼각형은 다른 색으로 채워져있따
turtle.left(90)
turtle.forward(100)
for i in range(0,3):
    if i==0:
        turtle.color("black","red")
    elif i==1:
        turtle.color("black","orange")
    elif i==2:
        turtle.color("black","yellow")
    turtle.right(180)
    turtle.forward(100)
    turtle.begin_fill()
    for j in range(0,3):
        turtle.forward(100)
        turtle.right(120)
turtle.exitonclick()
