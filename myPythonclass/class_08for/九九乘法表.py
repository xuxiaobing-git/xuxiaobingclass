# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 22:48
# @File    : 九九乘法表.py
# @Software: PyCharm
def multiplication_table():
    """九九乘法表"""
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("{} * {} ={}".format(col, row, row * col), end="\t")
            col += 1
        print("")
        row += 1
