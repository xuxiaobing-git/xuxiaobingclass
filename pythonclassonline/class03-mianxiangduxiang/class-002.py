# -*- encoding: utf-8 -*-
"""
@File    : class-002.py
@Time    : 2020/7/5 14:19
@Author  : XuXiaoBing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
"""
实例属性初始化方法
--init--:



"""


class Cat:
    leg = "有四条腿"
    tail = "有长尾巴"

    def __init__(self, name, age):  # 初始化方法：在创建对象时会自动调用
        print("__init__调用了")
        self.name = name
        self.age = age


# kt猫
kt = Cat(name="凯蒂", age=18)

# 叮当猫
dd = Cat(name="叮当", age=19)

print(kt.name)
print(kt.leg)
