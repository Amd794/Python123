# -*- coding: utf-8 -*-
# Time    : 2019/4/5 17:57
# Author  : Mifen
# Email   : 2952277346@qq.com
# Software: PyCharm

from turtle import *
import random
length = 1000
setup(1280,720)
up()
color("#0fe6ca")
goto(-600, 300)
write('Author:Mifen', font=("微软雅黑", 18))
goto(-600, 250)
write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
goto(0,0)
down()
def draw_path(path,y):
    up()
    goto(-500,200)
    sety(-y)
    down()
    pensize(2)
    colormode(255)
    color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for symbol in path:
        if symbol == 'A':
            fd(length/len(path))
        elif symbol == 'B':
            up()
            fd(length/len(path))
            down()
    ht()
def apply_path(rules,path):
    lit = [_ for _ in path]
    for i in range(len(lit)):
        symbol = lit[i]
        if symbol in rules:
            lit[i] = rules[symbol]
    path = ''.join(lit)
    return path
path = 'A'
rules = {
    'A':'ABA',
    'B':'BBB'
}
speed(0)
path_list = ['A']
n = 8
for i in range(n):
    path = apply_path(rules, path)
    path_list.append(path)
for y in range(0,n*10,10):
    draw_path(path_list.pop(0),y)
exitonclick()