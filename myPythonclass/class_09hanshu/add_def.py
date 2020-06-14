# -*- encoding: utf-8 -*-
"""
@File    : add_def.py
@Time    : 2020/6/14 15:43
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""


def add_1(a, b):
    Sum = 0
    for i in range(b):
        Sum += a
    return Sum


m = int(input("请输入第一个数值："))
n = int(input("请输入第二个数值："))
Num = add_1(m, n)
print("{}和{}的积等于:{}".format(m, n, Num))
