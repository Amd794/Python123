# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:44
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


from turtle import *
import random
import time

str_ = """
守一段情 念一个人。
时光不老 我们不散。
厮守终生 不离不弃。
天暗下来 你就是光。
亡魂溺海 止于终老。
生死挈阔 与子成说。
柔情似水 佳期如梦。
我中有你 你中有我。
青山不老 为雪白头。
心若向阳 无畏悲伤。
一人一心 白首不离。
心如荒岛 囚我终老。
我的世界 只有你懂。
你若安好 便是晴天。
心有灵犀 一点就通。
厮守海角 非你不娶。
执子的手 漫漫的走。
执子之手 与子偕老。
山河拱手 为君一笑。
红尘初妆 山河无疆。
千秋功名 一世葬你。
既不回头 何必不忘。
既然无缘 何须誓言。
今日种种 似水无痕。
明夕何夕 君已陌路。
才会相思 便害相思。
人来人往 繁华似锦。
回首万年 情衷伊人。
生能尽欢 死亦无憾。
执手若无 泪溅花上。
花开花落 人世无常。
入我心者 待以君王。
为醉而醉 似醉非醉。
伤心鸿影 爱已惘然。
只要你要 只要我有。
日久生情 日久情疏。
忧佳相随 风雨无悔。
有生之年 誓死娇宠
引喻山河 指日可诚。
水上鸳鸯 云中翡翠。
天荒地老 海誓山盟。
生则同襟 死则同穴。
生有此女 夫复何求""".split("。")
setup(1280,720)  # 设置窗口大小
colormode(255)  # 使用的颜色模式, 整数还是小数
up()
a, b = -500, 280
goto(a,b)
bgcolor("black")


down()
def w(str_,b):
    bgcolor( random.randint(0,255),random.randint(0,255),random.randint(0,255))  # 随机生成RGB值, 每次调用函数改变背景颜色
    for i in range(len(str_)):
        up()
        goto(a+100*i,b)
        down()
        size =  random.randint(12,68)  # 随机字体大小
        color( random.randint(0,255),random.randint(0,255),random.randint(0,255))  # 随机字体颜色
        write(str_[i], align="center",font=("楷体",size))

        
for k in range(4):
    for i in range(7):
        w(str_[i+7*k],b-100*i)
    reset()  # 清屏

    
for i in range(7):
    w(str_[i+7*4],b-100*i)
up()
color("#262626;")
goto(-600,300)
write('Author:Mifen',font=("微软雅黑", 18))
goto(-600,250)
write('E-mail :2952277346@qq.com',font=("微软雅黑", 18))
goto(-600, 200)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
goto(-600,-350)
down()
ht()
