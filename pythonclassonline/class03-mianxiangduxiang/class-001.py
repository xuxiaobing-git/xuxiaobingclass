# -*- encoding: utf-8 -*-
"""
@File    : class-001.py
@Time    : 2020/7/4 16:41
@Author  : XuXiaoBing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
"""class 类 类里面包含 属性和函数
class 类名（object）
属性:
    类属性：每个实例对象都有，而且值都一样，直接定义在类里面的变量
    实例属性：通过  实例对象.属性名   进行赋值的属性叫实例属性，实例对象是该实例对象独有的
             其他的对象获取不到
方法
"""


def swimming():
    print("喜欢游泳")


def coding():
    print("会写代码")


class Boyfriend:  # 类名的规范  大写字母开头，如果多个单子组成，每个单词第一个大写
    # 类属性
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


bf = Boyfriend()
coding()
# 实例属性
bf.cooking()
# print(bf.height)
# print(bf.money)
Boyfriend.cooking()
print(Boyfriend.age)
bf.hiking()
