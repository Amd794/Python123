# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:20
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


import pathlib
import sys

sys.path.append(pathlib.Path())
from BaseLsystem import Pic

rules = {
    'F': 'aFF-[b-F+F]+[c+F-F]',
    'X': 'aFF+[b+F]+[c-F]'
}
angle = 25
init_path = 'FX'
p = Pic(init_path, rules, angle)
apply_path = p.apply_rules()
p.draw_path(apply_path)
