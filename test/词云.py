#!/usr/bin/python
# -*- encoding:UTF-8-*-
# Turtle画图。
import turtle
#初始化参数
turtle.speed(10000)     #定义画笔速度
turtle.goto(0,0)    #去原点
# turtle.color('yellow','red')

#画一个边长为100的正方形，然后再以半径为50画出其3/4圆。
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# #turtle.home()   #回到原点
# turtle.circle(50,180)
# turtle.done()       #窗口保持！！

#360 个正方形每隔 1 度排列
for i in range(360):
    turtle.setheading(i)    #360度以1度旋转
    for i in range(4):      #不停地画正方形
        turtle.forward(100)
        turtle.right(90)
turtle.done()

#填充红五角星
# turtle.color('yellow','red')
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(100)
#     turtle.right(144)
# turtle.end_fill()
# turtle.done()
