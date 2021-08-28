# -*- coding: utf-8 -*-
# @Time : 2019/11/30 14:11
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_04_02.py
# @Project : xuxiaobingclass
# 字典  {}   关键字 dict
# a={}  空字典     格式   key  :value
a = {"name": "许小兵", "age": 30, "money": 99.99, "score": [100, 80, 100]}
print(type(a))
# 修改元素
a["sex"] = "man"
a["name"] = "Mixin"
print(a)
# 查询元素 1.键获取   2，get 方法
print(a['name'])
print(a.get("name"))
a["name"] = "学习的机会"
# 添加元素
a["class"] = "moju092"
print("修改之后的字典值：{}".format(a))
print("字典里面的姓名是：{0}".format(a["name"]))
# 删除字典元素
a.pop("age")
print("删除age之后的字典：{}".format(a))
print(a.keys())
print(a.values())
print(a.items())
c = {"name": "伪证", "age": "未知"}
a.update(c)
print(a)
print(a.items())
print(a.keys())
print(a.values())
print(a["score"][0])

str1 = 'runOob'
print(str1)  # 输出字符串
print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str1[0])  # 输出字符串第一个字符
print(str1[2:5])  # 输出从第三个开始到第五个的字符
print(str1[2:])  # 输出从第三个开始的后的所有字符
print(str1 * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str1 + "TEST")  # 连接字符串
