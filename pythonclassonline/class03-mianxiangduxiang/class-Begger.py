# -*- encoding: utf-8 -*-
"""
@File    : class-Begger.py
@Time    : 2020/7/8 11:36
@Author  : XuXiaoBing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
"""
学习地址：https://www.cnblogs.com/qflyue/p/8298555.html
"""

class Begger:
    count = 3  # 这是一个类属性

    def __init__(self, name, age, money):
        self.name = name  # 实例属性
        self.age = age
        self.money = money
        self._single = True  # 私有属性
        Begger.count += 1

    def beg(self):  # 定义一个要饭函数
        print("求各位给个馒头吃\n个人信息介绍:门派{}，年龄：{}，存款：{}".format(self.name, self.age, self.money))

    @staticmethod  # 静态方法
    def beg_skill():  # 定义一个乞讨技巧函数，静态方法
        print("乞讨技巧")

    @classmethod  # 类方法
    def beg_counter(cls):
        print("小乞丐个数：%s" % Begger.count)


if __name__ == '__main__':
    zm = Begger('古墓派掌门', '18', -10)
    zm.beg()
    print("小乞丐个数：{}".format(Begger.count))
    #   print(zm.name)
    zm.beg_skill()
    Begger.beg_counter()
