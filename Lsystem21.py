# -*- coding: utf-8 -*-
# Time    : 2019/4/6 16:25
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


# -*- coding: utf-8 -*-
# Author  : Mifen
# Email   : 2952277346@qq.com
# Date  : 2018/9/7


import turtle as t
import random

def draw_path(length, angle, path, expalnation):
    posList, angleList = [], []
    for symbol in path:
        # print(expalnation[symbol])
        if symbol == 'F':
            t.color(getColor(),getColor(),getColor())
            t.forward(length)
        elif symbol == '+':
            t.left(angle)
        elif symbol == '-':
            t.rt(angle)
        elif symbol == '[':
            posList.append(t.pos())
            angleList.append(t.heading())
        elif symbol == 'a':
            t.pensize(4)
            t.color("#8c503c")
        elif symbol == 'b':
            t.color("#4ab441")
            t.pensize(3)
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
    path = ''.join(L)
    return path


def getColor():
    t.colormode(255)
    return random.randint(0,255)


def Introduction(x=-600, y=-350):
    t.up()
    t.color(getColor(),getColor(),getColor())
    t.goto(-600, 300)
    t.write('Author:Mifen', font=("微软雅黑", 18))
    t.goto(-600, 250)
    t.write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
    t.goto(-600, 200)
    t.write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
    t.goto(x, y)
    t.down()


def initialization():
    t.setup(1280, 720)
    t.bgcolor("black")
    t.speed(0)
    t.pensize(1)


def run(n,angle,length,path,rules):
    initialization()
    Introduction(200,-100)
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
    for _ in range(n):
        path = apply_rules(path, rules)
    draw_path(length,angle,path, expalnation)
    t.done()


if __name__ == '__main__':
    angle = 90
    length = 20
    path = 'F+F+F+F' #初始路径
    rules = {
        'F': 'F+F-F-FF+F+F-F'  #转换规则
    }
    run(2,angle,length,path,rules)



