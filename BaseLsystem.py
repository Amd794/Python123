# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/12/12 15:25
# Author  : Amd794
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794
# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:20
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


import turtle as t


class Pic(object):
    def __init__(self,
                 init_path: str,
                 rules: dict,
                 angle: int,
                 length: int = 5,
                 deep: int = 5) -> None:
        t.setup(1280, 720)
        t.speed(0)
        t.pensize(1)
        self.deep = deep
        self.about_me()
        self.length = length
        self.init_path = init_path
        self.angle = angle
        self.rules = rules

    def about_me(self):
        t.up()
        t.color("#262626")
        t.goto(-600, 300)
        t.write('Author:Amd794', font=("微软雅黑", 18))
        t.goto(-600, 250)
        t.write('E-mail :2952277346@qq.com', font=("微软雅黑", 18))
        t.goto(-600, 200)
        t.write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
        t.goto(-600, -350)
        t.down()

    def draw_path(self, apply_path):
        posList, angleList = [], []
        t.up()
        t.goto(0, -350)
        t.down()
        t.lt(90)
        for symbol in apply_path:
            if symbol == 'F':
                t.forward(self.length)
            elif symbol == '+':
                t.left(self.angle)
            elif symbol == '-':
                t.rt(self.angle)
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

    def apply_rules(self):
        apply_path = self.init_path
        for k in range(self.deep):
            L = [_ for _ in apply_path]
            for i in range(len(L)):
                symbol = L[i]
                if symbol == 'F':
                    L[i] = self.rules[symbol]
                if symbol == 'X':
                    L[i] = self.rules[symbol]
            apply_path = ''.join(L)
        return apply_path


if __name__ == '__main__':
    rules = {
        'F': 'aFF-[b-F+F]+[c+F-F]',
        'X': 'aFF+[b+F]+[c-F]'
    }
    angle = 25
    init_path = 'FX'
    p = Pic(init_path, rules, angle)
    apply_path = p.apply_rules()
    p.draw_path(apply_path)
