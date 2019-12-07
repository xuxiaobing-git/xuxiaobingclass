# -*- coding: utf-8 -*-
# @Time : 2019/12/7 21:06
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_09_03_positional_arg.py
# @Project : xuxiaobingclass

def  print_msg(a,b):#位置参数  /形参
    print(a)
    print(b)
    print("我谁都不用")
print_msg("a：a的值","b:b的值")
#print_msg("你好啊","我不好")
#如果是位置参数：有几个参数，就要传递几个参数，例如 print_msg("a：a的值") 会报错
##############位置参数是按顺序赋值
##############传递的参数使用顺序不一定按照顺序
##############可以不按顺序赋值，通过关键字赋值
def add_3(m,n,k):
    count=0
    for  i  in  range (m,n,k):
         count+=i
    print("求和结果是(函数内部)：",count)
    return  count
result=add_3(0,101,2)
print("计算结果是：",result)
