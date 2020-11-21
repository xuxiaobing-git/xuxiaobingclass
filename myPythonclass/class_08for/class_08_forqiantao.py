# -*- coding: utf-8 -*-
# @Time : 2019/12/7 16:00
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_08_forqiantao.py
# @Project : xuxiaobingclass

# 嵌套for循环
list_1 = [[2, 5, 9, 7, ], [12, 45, 19, 16, 13, ]]
for item in list_1:
    for value in item:
        print("数据：", value)
        # print("数据类型", type(value))
# 打印出三角形  底边长度为5
for g in range(1, 6):
    # print("现在是第{}行".format(g))
    for p in range(g):
        print("* ", end="")  # 控制不换行输出
    print("")  # 控制for循环结束后    换行
# 99乘法表
for i in range(1, 10):  # 控制行数
    for j in range(1, i + 1):  # i=1  j=1     i=2  j=1  2    i=3   j=1  2   3
        print("{0}*{1}={2} ".format(j, i, i * j), end="\t")  # 控制次for循环里面的内容不换行
    print("")  # for循环结束时换行
