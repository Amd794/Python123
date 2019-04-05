# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:29
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794



import time
import turtle as t
from turtle import *
t.setup(1280,720)
t.speed(0)
t.pensize(1)
length = 8
path = 'F-F-F-F-F'
angle = 72
up()
color("blue")
goto(-600, 300)
write('Author:Mifen', font=("微软雅黑", 18))
goto(-600, 250)
write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
goto(-600, 200)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
goto(-600, -350)
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
    'F': 'F-F++F+F-F-F',
    'X': 'aF-[b[X]+cX]+aF[c+FX]-X'
}


def draw_path(path, expalnation):
    posList, angleList = [], []
    t.up()
    t.bgcolor("black")
    t.goto(400,0)
    t.down()
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
    path = ''.join(L)
    return path


for _ in range(4):
    path = apply_rules(path, rules)
draw_path(path, expalnation)