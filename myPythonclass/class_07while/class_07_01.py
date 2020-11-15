# -*- coding: utf-8 -*-
# @Time : 2019/12/6 23:05
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_07_01.py
# @Project : xuxiaobingclass
# while循环
# a = 9
# while a < 10:
#     print("我是循环")
# 死循环
# while循环是先判断 再执行  执行完再判断
# a = 9
# while a > 0:
#     print("我是while循环{}".format(a))
#     a -= 1
b = 1
Sum = 0
while b < 101:
    Sum = Sum + b
    b = b + 1
print("1-100的整数和：{}".format(Sum))
# a = 10
# while True:
#     a -= 1  # 每次对a减去1  a=a-1
#     if a > 0:
#         print("a的值：{}".format(a))
#         continue
#     else:
#         break
count = 2  #增加循环次数
while count:
    users = {"user": "admin", "pwd": "1234"}
    user = input("请输入登录名：")
    pwd = input("请输入密码：")
    if user == users.get("user"):
        if pwd == users.get("pwd"):
            print("登录成功")
            break
        else:
            print("密码不对")
    else:
        count -= 1
        print("你还有剩余{}次输入机会".format(count))
        print("账号不正确")
