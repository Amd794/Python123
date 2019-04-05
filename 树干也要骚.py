# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:38
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


import turtle

toplevel = 6  # 一共递归6层
angle = 30


def drawTree(length, level):
    turtle.left(angle)  # 绘制左枝
    turtle.forward(length)

    if level < toplevel:  # 在左枝退回去之前递归
        drawTree(length - 10, level + 1)
    turtle.back(length)

    turtle.right(angle * 2)  # 绘制右枝
    turtle.forward(length)

    if level < toplevel:  # 在右枝退回去之前递归
        drawTree(length - 10, level + 1)
    turtle.back(length)
    turtle.left(angle)

turtle.speed(1)
turtle.tracer(0)  # 不刷新
turtle.left(90)
drawTree(80, 1)
turtle.update()  # 刷新，和上面的tracer(0)配合，直接出图形，忽略过程

turtle.done()