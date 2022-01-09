"""파일명: turtle graphic
   작성자: koo-bon-sik  """

import turtle

width=int(input("width = ")) #가로
length=int(input("length = ")) #세로

turtle.setup(500,500) #set width and height of canvas
t=turtle.Turtle()
t.shape("turtle") #객체의 모양
t.pencolor("red")
t.width(10) 

#t.up() : 터틀의 펜을 위로 들어 이동에 따른 그리기가 나타나지 않게 함
#t.down() : 터틀의 펜을 위로 들어 이동에 따른 그리기가 나타나게 함
#t.goto(x,y) : x,y로 이동 , canvas의 중심좌표로 부터
t.up(); t.goto(-width/2, length/2); t.down() 

count =0
angle_turn= 360/4
while count < 2:
    t.forward(width)
    t.right(angle_turn)
    t.forward(length)
    t.right(angle_turn)
    count =count +1

t.up(); t.goto(0,0); t.down()


"""
파일명: tutle graphic
작성자: Koo-bon-sik
<problem>
정 삼각형의 한 변의 길이 (length)를 입력 받고, 터틀 그래픽 화면 중앙에 정삼각형을 그리는 파이썬 프로그램을 작성하라. 삼각형의 좌측 하단 꼭지점의 좌표를 정확하게 계산하여 출
력하며, 터틀 그래픽의 중앙과 정 삼각형의 각 꼭지점 좌표를 터틀 객체의 write() 함수를 사용하여 출력할 것..
"""
import turtle
import math
turtle.setup(500,500)

t=turtle.Turtle()
t.shape('turtle')
t.pencolor('red')
t.width(10)

length=int(input("input side length of triangle = "))
t.up(); t.goto(-length/2,-((length/2)*math.tan(math.pi/6)))
label=t.position() #현재 위치를 가져옴
t.write(label) ;t.down() #canvos위에 좌표 표시
print("x0, y0 = ",label )

count =0
angle=180/3 *2
while count <3:
    t.forward(length)
    t.left(angle)#반시계 방향으로 각도만큼 
    t.write(t.position())
    count = count +1

t.up()
t.home() #중심좌표로 이동
t.write(t.position()) #canvos위에 좌표 표시

input("press any key to key") #키 입력시 tutle graphic 종료

"""
파일명: drawPolygon
작성자: Koo-Bon_sic
problem : 파이썬 터틀 그래픽 기능을 사용하여 지정된 위치에 지정된 크기 (한 변의 길이)의 다각형을 그리는 drawPolygon() 함수를 구현하라. 이 함수에 전달되는
인수로는 중심 위치 (x좌표, y좌표), 다각형의 꼭지점 수, 다각형 한 변의 길이가 주어지도록 하라. 입력된 중심 위치와 다각형의 시작 위치 및 각 꼭지점
에 붉은색 점 (dot)을 표시하고, 각 꼭지점의 좌표값을 출력하라.
"""

import turtle
import math

def drawPolgon(t, x ,y, dot_num, length):
    t.penup(); t.goto(x,y) ; t.dot(10,"red")
    t.write(t.position())
    
    angle= 360//dot_num
    t.goto(-(length/2), -(length/2)*(math.tan(math.radians((540/5)/2)))) #; t.dot(10,"red")
    t.pendown()
    
    for i in range(dot_num) :
        t.forward(length)
        t.left(angle)
        t.dot(10,"red")
        t.write(t.position())

    t.penup(); t.goto(x,y); t.pendown()

#setting
t =turtle.Turtle()
t.shape('classic')
t.color('blue')
t.width(10)

dot_num,length = map(int,input("input dot_num, lengh:").split(' '))
drawPolgon(t, 0, 0, dot_num, length)
input("exit")

    
    

          

