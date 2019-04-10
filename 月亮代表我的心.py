# -*- coding: utf-8 -*-
# Time    : 2019/4/6 22:45
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


from turtle import *
import time
import turtle as t


def gotopos(x, y):
    up()
    goto(x, y)
    down()
    ht()


def author():
    pensize(2)
    gotopos(610, -315)
    lt(-90)
    fd(80)
    pensize(1)
    lt(-270)
    gotopos(525, -330)
    color("#772a2b")
    write("Mifen", font=("华文隶书", 24))
    gotopos(409, -360)
    write("2952277346@qq.com", font=("华文隶书", 18))
    gotopos(250, -390)
    write("https://github.com/Amd794/Python123", font=("华文隶书", 18))


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


def draw_path(path):
    posList, angleList = [], []
    for symbol in path:
        if symbol == 'F':
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
            t.color("#867b68")
        elif symbol == 'b':
            t.pensize(2)
            t.color("#867b68")
        elif symbol == 'c':
            t.pensize(2)
            t.color("#867b68")
        elif symbol == ']':
            t.up()
            t.home()
            t.goto(posList.pop())
            t.left(angleList.pop())
            t.down()


def writez(x, y, str_, size=56, font="华文行楷"):
    gotopos(x, y)
    write(str_, font=(font, size))
setup(1280,800)
speed(5)
bgcolor("#9c917f")
color("#afa697")
begin_fill()
gotopos(0, -400)
circle(400)
end_fill()
author()
color("#7d776d")
s = "愿天化作比翼鸟"
s2 = "在地愿为连理枝"
for i in range(len(s)):
    writez(560,350-i*50,s[i],36)
for i in range(len(s2)):
    writez(460,350-i*50,s2[i],36)
color("#888475")
writez(-50, 100, "我")
writez(-50, 40, "的")
writez(-160, 0, "心", 96)
writez(-50, 0, "月", 176)
writez(33, -30, "代", 62)
writez(-18, -95, "表", 78)
writez(-213, -210, "亮", 196)

gotopos(249, -26)
color("#867b68")
speed(0)
gotopos(-650, -100)
length = 6
path = 'F'
angle = 27
rules = {
'F': 'aFF[b-F++F][c+F--F]c++F--F',
'X': 'aFF+[b+F]+[c-F]'
}

for _ in range(4):
    path = apply_rules(path, rules)
draw_path(path)
gotopos(570, -330)
done()