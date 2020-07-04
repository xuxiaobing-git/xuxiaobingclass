# -*- encoding: utf-8 -*-
"""
@File    : default-01.py
@Time    : 2020/7/4 16:18
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
"""异常捕获"""
try:
    print(a)
except NameError as e:
    print("异常")
else:
    print("代码未报错")
