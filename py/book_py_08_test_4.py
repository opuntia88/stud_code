import turtle

scr=turtle.Screen()
scr.bgcolor("white")
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
#turtle.penup()
#turtle.left(180)
#turtle.forward(100)
#turtle.pendown()
for i in range(0,3):
    turtle.penup()#펜을 띄운다.
    if i==0:#각 도형의 색을 다르게 한다.
        turtle.color("black","red")
    elif i==1:
        turtle.color("black","orange")
    elif i==2:
        turtle.color("black","yellow")
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()#도형을 그릴 점부터 선을 내린다.
    turtle.begin_fill()#그릴 도형에만 색상을 씌운다.
    for j in range(0,3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()
    
turtle.exitonclick()
