# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:32
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794



import time
import turtle as t
from turtle import *

t.speed(0)
t.pensize(1)
length = 40
path = 'F'
angle = 90
setup(1280,720)
up()
color("blue")
goto(-600, 300)
write('Author:Mifen', font=("微软雅黑", 18))
goto(-600, 250)
write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
goto(-600, 200)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
goto(0,0)
down()
expalnation = {
    'F': '画线',
    'x': '-',
    '+': '逆时针旋转',
    '-': '顺时针旋转',
    '[': '记录当前位置',
    ']': '恢复上一个位置',
    'a': '上色',
    'b': '上色',
    'c': '上色'
}
rules = {
    'F': 'F+F-F-F-G+F+F+F-F',
    'G': 'GGG'
}


def draw_path(path, expalnation,angle):
    posList, angleList = [], []
    t.bgcolor("black")
    t.lt(90)
    for symbol in path:
        if symbol == 'F':
            import random
            colormode(255)
            color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            t.forward(length)
        elif symbol == '+':
            t.left(angle)
        elif symbol == '-':
            t.rt(angle)
        elif symbol == '[':
            posList.append(t.pos())
            angleList.append(t.heading())
        elif symbol == 'a':
            t.pensize(3)
            t.color("#8c503c")
        elif symbol == 'b':
            t.pensize(2)
            t.color("#4ab441")
        elif symbol == 'c':
            t.pensize(2)
            t.color("#18b418")
        elif symbol == 'G':
            angle = -angle
        elif symbol == ']':
            t.up()
            t.home()
            t.goto(posList.pop())
            t.left(angleList.pop())
            t.down()


def apply_rules(path, rules):
    L = [_ for _ in path]
    for i in range(len(L)):
        symbol = L[i]
        if symbol == 'F':
            L[i] = rules[symbol]
        if symbol == 'X':
            L[i] = rules[symbol]
        if symbol == 'G':
            L[i] = rules[symbol]
    path = ''.join(L)
    return path


for _ in range(5):
    path = apply_rules(path, rules)
draw_path(path, expalnation,angle)