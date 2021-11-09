# -*- coding: utf-8 -*-
# @Time : 2019/12/7 15:07
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_08.py
# @Project : xuxiaobingclass
s = "lemon"  # 字符串
L = ["lemon", "python"]  # 列表
t = (1, 2, 3, 0, 4, "hi")  # 元组
d = {"name": "柠檬班冰冰", "course": "pyhon全栈自动化"}  # 字典
for em in d:  # 遍历in后面的数据类型里面的每一个元素   依次挨个
    print("****em****:", em)
for item in d.values():
    print("****item*********:", item)
for item in d:
    print("****item**********************:", d[item])

# 小练习：1-100相加和
# range函数   range（m,n,k） m开头  n结尾 k步长
m = "hello"
print(m[0:5:2])
print(list(range(0, 5, 2)))  # 0  2  4
print(list(range(0, 10, 3)))  # 0  3  6  9
print(list(range(2, 6)))  # k默认为1
print(list(range(6)))  # 只传一个     m默认为0    k默认1

count = 0
for item in range(1, 101):
    count += item
print("0-100的求和：{}".format(count))

f = ["我", "爱", "中", "国", "共", "产", "党"]
for i in range(6, -1, -1):
    print(f[i],end="\t")
