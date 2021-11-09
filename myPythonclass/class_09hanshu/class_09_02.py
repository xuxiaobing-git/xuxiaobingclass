# -*- coding: utf-8 -*-
# @Time : 2019/12/7 20:38
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_09_02.py
# @Project : xuxiaobingclass

# def add():
#     print(8 + 9)
#
#
# def add_1():
#     return 9 + 9
#
#
# print("第一个函数的结果***")
# add()
# print(add())
# print("第二个函数的结果***")
# result = add_1()
# print("add_1的函数的结果：", result)


# return的作用：当你调用这个函数时候  会返回一个结果，这个结果值
# 当你需要使用时可以做后续的继续处理
# 如果没有 return的话   那么返回结果就是none
# 小练习：利用for循环   range 函数  编写任意整数序列的求和函数
def add_3():
    count = 0
    for i in range(1, 101, 1):
        count = count + i
    print("求和结果是(函数内部)：", count)
    return count, 6666


result2 = add_3()
print("最终运算结果：", result2)
