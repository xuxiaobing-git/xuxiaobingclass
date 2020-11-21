# -*- coding: utf-8 -*-
# @Time : 2020/4/6 19:56
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_10_03初始化函数.py
# @Project : xuxiaobingclass
def coding(language):
    print("会写{0}代码".format(language))


class Boyfriend:
    # 属性666
    def __init__(self, height, money, name, age):
        self.height = height
        self.money = money
        self.name = name
        self.age = age

    @classmethod  # 类方法
    def cooking(cls):
        print("会做饭")

    @staticmethod  # 静态方法
    def hiking():
        print("喜欢户外运动")

    # 实例方法
    def swimming(self):
        print(self.name + "喜欢游泳")


bf = Boyfriend(180, 200000, "nick", 22)
coding("python")
bf.swimming()
