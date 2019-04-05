# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:12
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794

from turtle import *
import random
length = 10
angle  = 90
setup(1280,720)
up()
color("#262626;")
goto(-600,300)
write('Author:Mifen',font=("微软雅黑", 18))
goto(-600,250)
write('E-mail :2952277346@qq.com',font=("微软雅黑", 18))
goto(-600, 200)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
goto(-640,-360)
down()
def draw_path(path):
    for symbol in path:
        if symbol == 'f':
            colormode(255)
            color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            fd(length)
        elif symbol == '+':
            lt(angle)
        elif symbol == '-':
            rt(angle)

def apply_path(rules,path):
    lit = [x for x in path]
    for i in range(len(lit)):
        symbol = lit[i]
        if symbol == 'x':
            lit[i] = rules[symbol]
        elif symbol == 'y':
            lit[i] = rules[symbol]
    path = ''.join(lit)
    return path

rules = {
    'x':'+yf-xfx-fy+',
    'y':'-xf+yfy+fx-'
}
path = 'x'
speed(0)
for i in range(7):
    path = apply_path(rules,path)
draw_path(path)
done()