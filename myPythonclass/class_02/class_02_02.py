# -*- coding: utf-8 -*-
# @Time : 2019/11/22 23:06
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_02_02.py
# @Project : xuxiaobingclass

#  字符串的替换 replace()
str_1 = "mlemonmmmommmm"
res = str_1.replace("o", "test", )
print("替换后的结果：{}".format(res))
res2 = str_1.split('o')
print("切割字符串：{}".format(res2))
res3 = str_1.strip("m")  # strip函数只处理头和尾
print("处理后的字符串：{}".format(res3))
