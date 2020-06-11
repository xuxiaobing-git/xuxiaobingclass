# -*- coding: utf-8 -*-
# @Time : 2019/12/3 22:26
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_06_01.py
# @Project : xuxiaobingclass
# age=56
# # if  age>=18:
# #     print("已经18啦")
# # else:
# #     print(age)
"""
if  条件判断语句
"""
# color=input("请输入红绿灯颜色")
# #color="yellow"
# if color=="red":
#     print("红灯停")
# elif color=="green":
#     print("绿灯行")
# elif color=="yellow":
#     print("黄灯停一停")
# else:
#     print("无此信号灯")

"""登录小案例"""
users = {"user":"xuxiaobing","pwd":"123456"}
user = input("请输入登录名：")
pwd = input("请输入密码：")
if user==users.get("user"):
    if pwd == users.get("pwd"):
        print("登录成功")
    else:
        print("密码不对")
else:
    print("账号不正确")
