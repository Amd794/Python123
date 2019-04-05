import turtle as t
from turtle import *
import random



def draw_path(path):
    t.colormode(255)
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for symbol in path:
        if symbol == 'F':
            forward(length)
        elif symbol == '-':
            right(angle)
        elif symbol == '+':
            left(angle)

def apply_rule(path):
    rule = 'F+F--F+F'
    return path.replace('F',rule)

length = .5
angle  = 60
setup(1280,720)
bgcolor('black')
up()
color("#0fe6ca")
goto(-600, 300)
write('Author:Mifen', font=("微软雅黑", 18))
goto(-600, 250)
write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
goto(0,0)
down()
path = 'F--F--F'
speed(0)
up()
goto(-440,-250)
down()
for i in range(5):
    path = apply_rule(path)
draw_path(path)
draw_path(path)
draw_path(path)
a,b = pos()
for i in range(3):
    up()
    a += 250
    goto(a,b)
    down()
    draw_path(path)
    draw_path(path)
    draw_path(path)
b += 220
for i in range(2):
    up()
    a -= 250
    goto(a,b)
    down()
    draw_path(path)
    draw_path(path)
    draw_path(path)
b += 220
for i in range(2):

    draw_path(path)
    draw_path(path)
    draw_path(path)
    up()
    a += 130
    goto(a,b)
    down()
