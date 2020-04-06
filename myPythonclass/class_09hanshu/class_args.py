# -*- coding: utf-8 -*-
# @Time : 2020/4/6 16:58
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_args.py
# @Project : xuxiaobingclass
#不定长参数/动态参数
def  add(*args):
    print(args)
    print("arge的类型",type(args))
add(1,2,3,4,5,6,)