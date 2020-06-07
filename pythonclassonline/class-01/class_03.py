# -*- encoding: utf-8 -*-
"""
@File    : class_03.py
@Time    : 2020/6/7 13:31
@Author  : XXX
@Email   : XXXX@163.com
@Software: PyCharm
"""
# 数据列表
# 标志  []  关键字  list    列表内可以是任意类型
# a =[]  空列表
# 列表的取值：也是根据索引来取值
a = [1, 0.05, "lemonBan", (1, 2.3, 5), [4, 5, 6]]
print(a[2])
print(a[-1])
# 列表的切片
print(a[0::2])
print(a[-1][-1])
# 列表的判断语句
print(2 in a)
# 就是就是计算机
# 修改之后
print(1 in a)
print(0.05 in a)
print(a)
# li = ["周一", "周二", "周三", "周四", "周五", "周末", "周末"]
# num = int(input("请输入1-7："))
# print("今天是：{}".format(li[num - 1]))
li2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
li2.insert(4, 66)
li2.extend([11, 22, 33])
print(li2)
li2.sort(reverse=False)
print(li2)
print(li2[2::3])
