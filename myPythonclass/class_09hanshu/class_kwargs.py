# -*- coding: utf-8 -*-
# @Time : 2020/4/6 17:22
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_kwargs.py
# @Project : xuxiaobingclass
# 参数类型：key   values
# 关键字参数 **kwargs
def lemon_info(**kwargs):
    print("kwargs:", kwargs)
    for item in kwargs.values():
        print(item)


lemon_info(t_name="华华", t_class="林蒙班", t_course="python")
