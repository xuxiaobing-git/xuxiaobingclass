# -*- coding: utf-8 -*-
# @Time : 2019/12/8 19:01
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_09_04default.py
# @Project : xuxiaobingclass
#默认参数
def greet(name ,content="敢问路在何方"):
    '''此函数是向不同的用户发问候'''
    print(name +content)
# greet("华华","下午好")
greet("上帝!")
#1，带有默认值的参数  必须在位置参数后面
#2，默认参数可以有多个   是在条件1的前提下
#3，如果有默认值   这个参数可以不传值
#4，按顺序赋值   也可以通过关键字指定赋值