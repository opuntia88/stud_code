#8.turtle: 터틀을 이용하여 그림을 그릴 수 있다. 
import turtle

#오각형을 그리는 코드
scr=turtle.Screen()#배경 윈도우의 이름을 정의
scr.bgcolor("green")#배경색을 정함
turtle.shape("turtle")#그림을 그리는 점을 터틀로 지정. 지정을 안 할 경우 화살표가 된다.
turtle.color("yellow","blue")#노랑윤곽선에 파랑색 채우기가된 색상의 도형으로 채워진다.
turtle.pensize(3)#선의 굵기를 선정.

turtle.begin_fill()#그리는 모양안을 채워준다.
for i in range(0,5):#5각형이므로 5번 반복.
    turtle.forward(100)#100만큼 직진
    turtle.right(72)#72만큼 왼쪽으로 꺾음.
turtle.end_fill()#안을 채우는 작업이 중지되도록 파이썬에게 알려준다.

#turtle.exitonclick()#for문이 끝나면 터틀을 끝냄.
turtle.penup()#터틀에 움직임을 따르는 선이 사라짐.
turtle.left(90)
turtle.forward(200)
turtle.pendown()#터틀의 움직임에 따르는 선이 다시 생김


#중첩루프:담순한 모양을 안에서 중첩시키는 함수
turtle.hideturtle()
for i in range(0,10):#오각형을 그린 후 외부의 10각형의 선을 그리는 함수.
    turtle.right(36)
    for i in range(0,5):#오각형을 그리는 함수
        turtle.forward(100)
        turtle.right(72)
turtle.showturtle()#거북이를 다시 보여줌

#t=turtle.pen() #turtle 대신 t를 씀.->안됨
turtle.left(180)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.begin_fill()
for i in range(0, 9
):
    turtle.forward(30)
    turtle.right(40)
    for i in range(0,8):
        turtle.right(45)
        turtle.forward(50)
turtle.end_fill()
turtle.exitonclick()#사용자가 터틀 윈도우를 클릭하면 윈도우가 자동으로 닫힌다.