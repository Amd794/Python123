# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:06
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794

from turtle import *

import random
length = 2
angle  = 90
setup(1280,720)
up()
color("#262626;")
goto(-600,300)
write('Author:Mifen',font=("微软雅黑", 18))
goto(-600,250)
write('E-mail :2952277346@qq.com',font=("微软雅黑", 18))
goto(-600, 200)
write('代码 :https://github.com/Amd794', font=("微软雅黑", 18))
goto(-600,-350)
down()
def draw_path(path):
    for symbol in path:
        if symbol == 'F':
            colormode(255)
            color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            forward(length)
        elif symbol == '-':
            right(angle)
        elif symbol == '+':
            left(angle)
    ht()

def apply_rule(path):
    rule = 'F+F-F-F+F'
    return path.replace('F',rule)

path = 'F'
speed(0)
for i in range(5):
    path = apply_rule(path)
for i in range(5):
    draw_path(path)
up()
goto(-478,-228)
down()
for i in range(4):
    draw_path(path)
up()
goto(-356,-106)
down()
for i in range(3):
    draw_path(path)
up()
goto(-235,16)
down()
for i in range(2):
    draw_path(path)
up()
goto(-115,137)
down()
draw_path(path)
