# -*- coding: utf-8 -*-
# @Time : 2019/12/22 19:50
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_object01.py
# @Project : xuxiaobingclass
# class  类 类里面包含 属性和函数
class Boyfriend:
    height = 175
    money = 200000
    name = "周杰伦"
    age = 28

    @classmethod
    def cooking(cls):
        print("会做饭")

    # @staticmethod
    def hiking(self):
        print(self.name + "喜欢户外运动")

    def swimming(self):
        print("喜欢游泳")

    def coding(self):
        print("会写代码")


bf = Boyfriend()
bf.coding()
bf.cooking()
# print(bf.height)
# print(bf.money)
Boyfriend.cooking()
print(Boyfriend.age)
bf.hiking()
