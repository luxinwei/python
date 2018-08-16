# -*- coding:utf-8 -*-

# 用户输入2个数字，并计算2个数字之和

import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('两数之和为 %.1f' %(float(input('输入第一个数字：')) + float(input('输入第二个数字：'))))



