# -*- coding: utf-8 -*-
# Time    : 2019/4/6 16:25
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794

import pathlib
import sys

sys.path.append(pathlib.Path())
from BaseLsystem import Pic

angle = 90
rules = {
    'F': 'F+F-F-FF+F+F-F'  # 转换规则
}
init_path = 'F+F+F+F'
p = Pic(init_path, rules, angle, )
apply_path = p.apply_rules()
p.draw_path(apply_path)
