# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:40
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


import turtle as t
from turtle import *

angle = 60 #通过改变角度，绘制出各种多边形
t.bgcolor('black')
t.pensize(2)
randomColor = ['red','blue','green','purple','gold','pink']
t.speed(0)
for i in range(200):
      t.color(randomColor[i%6])
      t.circle(i)
      t.rt(angle+1)
up()
color("#0fe6ca")
goto(-600, 300)
write('Author:Mifen', font=("微软雅黑", 18))
goto(-600, 250)
write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
goto(-600, 200)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
goto(0,0)
down()