import turtle as t
from turtle import *


angle = 60 #通过改变角度，绘制出各种多边形
t.setup(1280,720)
t.bgcolor('black')
t.pensize(2)
randomColor = ['red','blue','green','purple','gold','pink']
t.speed(0)
for i in range(600):
      t.color(randomColor[i%6])
      t.fd(i)
      t.rt(angle+1)
up()
color("#0fe6ca")
goto(-600, 300)
write('Author:Mifen', font=("微软雅黑", 18))
goto(-600, 250)
write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
goto(0,0)
down()
t.done()
