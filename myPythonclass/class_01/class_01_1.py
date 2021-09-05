# -*- coding: utf-8 -*-
# @Time : 2019/8/27 23:21
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_01_1.py
# @Project : myPython

# print (a+b)
# print ('许  小   兵')
#
# print("999")
# a=4
# if  a>6:
#     print ('hello nihao')
# else:
#
#     print('true')
# print('hello')
# # # a=input('请输入你想要的文字  ')
#  print(a)
# a=1
# b=2
# c=a+b
# print(c)
# print(type(c))

# a="xuxiaobing"
# print(a[3])
#
# print(a[-1])
# print('b'in  a )


# a='lemon'
# #字符串切片
# res=a[0:4:1]
# print(res)
# resa=a[0:5:2]
# print(resa)

# str_1='123456789'
# print(str_1[1:10:2])


age = 30
name = "许小兵"
score = 99.99
print(name + '，年龄' + str(age) + "岁")
print(name + "，年龄", age, "岁")
print("%s，年龄%d岁,数学考了%.2f分" % (name, age, score))
print("{}年龄{}，数学考了{}".format(name, age, score))
print("{2}年龄{1}，数学考了{0}".format(name, age, score))

str_1="hello"
str_2="PYTHON"
res=str_1.upper()
res2=str_2.lower()
print("转换成大写:{}".format(res))
print("转换成小写：{}".format(res2))
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print(i,j,k)
