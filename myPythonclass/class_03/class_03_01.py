# -*- coding: utf-8 -*-
# @Time : 2019/11/23 14:30
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_03_01.py
# @Project : xuxiaobingclass
# 元组   标志 ()  关键字 tuple
# str_1="xuxiaobing"
# str_2=str_1.replace("ing","m")
# print("修改之后：{}".format(str_2))
import random

tuple_1 = (1, 0.022, "lemon", (1, 2, 3), [11, 22, 33])
# 元组里面可以是任何类型
# print(type(tuple_1))
print(tuple_1[2])
print(tuple_1[-1])
# 元组切片
print(tuple_1[1::2])
# 元组值一旦确定就无法  增  删  改
# 元组可以使用判断元素
print(1 in tuple_1)
# 元组内容有可变类型元素，可变类型元素可以修改
tuple_1[4].append(999)
print(tuple_1)
print(len(tuple_1))
a = random.randint(1, 100)
print(a)
