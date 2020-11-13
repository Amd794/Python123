# -*- coding: utf-8 -*-
# Author  : Mifen
# Email   : 2952277346@qq.com
# Date  : 2018/9/7


import time
import turtle as t
from turtle import *

t.setup(1280,720)
t.speed(0)
t.pensize(1)
length = 13
path = 'F' # 初始规则
angle = 22
up()
color("#262626;")
goto(-600,300)
write('Author:Mifen',font=("微软雅黑", 18))
goto(-600,250)
write('E-mail :2952277346@qq.com',font=("微软雅黑", 18))
goto(-600,-350)
down()
expalnation = {
      'F':'画线',
      'x':'-',
      '+':'逆时针旋转',
      '-':'顺时针旋转',
      '[':'记录当前位置',
      ']':'恢复上一个位置',
      'a':'上色',
      'b':'上色',
      'c':'上色'
      }
rules = {
       # 每一次迭代后 F 都将被替换为 aFF-[b-F+F+F]+[c+F-F-F]   ==> 如: 初始为F --第一次迭代后-->aFF-[b-F+F+F]+[c+F-F-F] --第一次迭代后-->a aFF-[b-F+F+F]+[c+F-F-F] aFF-[b-F+F+F]+[c+F-F-F] -太长不写了 
      'F':'aFF-[b-F+F+F]+[c+F-F-F]' 
      }

      
def draw_path(path,expalnation):
      posList ,angleList= [],[]
      t.up()
      t.goto(0,-350)
      t.down()
      t.lt(90)
      for symbol in path:
            if symbol == 'F':
                  t.forward(length)  # 向前画出length长度
            elif symbol == '+': 
                  t.left(angle)   # 向左边旋转出angle角度
            elif symbol == '-':
                  t.rt(angle)  # 向右边旋转出angle角度
            elif symbol == '[':
                  posList.append(t.pos())  # 记录当前位置的坐标值,将当前的坐标值放到一个列表中
                  angleList.append(t.heading())  # 记录当前位置的角度值,将当前的角度值放到一个列表中
            # abc分别代表树干 树枝和树叶的颜色
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
                  t.goto(posList.pop())  # 复原最近添加的一个坐标值
                  t.left(angleList.pop())  # 复原最近添加的一个角度值
                  t.down()

def apply_rules(path,rules):
      L = [_ for _ in path]
      for i in range(len(L)):
            symbol = L[i]
            if symbol == 'F':
                  L[i] = rules[symbol]
      path = ''.join(L)
      return path


for _ in range(4):
      path = apply_rules(path,rules)  # 获取迭代4此后的最总规则, 一串很长的字符串
draw_path(path,expalnation) # 开始绘画

