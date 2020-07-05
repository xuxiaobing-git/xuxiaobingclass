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
    类属性和实例属性的访问: 
         类属性可以通过实例对象访问
         类属性也可以直接通过类去访问
         实例属性只能通过实例访问
                    
方法:定义在类中的函数
对象：
"""


class Boyfriend:  # 类名的规范  大写字母开头，如果多个单子组成，每个单词第一个大写
    # 类属性
    height = 175
    money = 200000
    name = "周杰伦"
    age = 28

    # 实例方法
    def skill1(self):  # self:代表实例对象
        print("技能1 ：看家")

    def skill2(self):
        print("技能2 ：做饭")


b1 = Boyfriend()
b2 = Boyfriend()
b1.code = "写代码"
b2.code = "不会写代码"
print("---------b1----------")
print(b1.code)
print(b1.name)
print("---------b2----------")
print(b2.code)
print(b2.name)
# 类属性也可以直接通过类去访问
print(Boyfriend.money)
# 通过实例对象来调用实例方法
b1.skill1()

# 通过类来调用实例方法：需要传入一个实例对象
Boyfriend.skill1(b1)
