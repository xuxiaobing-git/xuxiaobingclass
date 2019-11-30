# -*- coding: utf-8 -*-
# @Time : 2019/11/30 14:11
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_04_02.py
# @Project : xuxiaobingclass
#字典  {}   关键字 dict
# a={}  空字典     格式   key  :value
a={"name":"许小兵","age":30,"money":99.99,"score":[100,80,100]}
print(type(a))
a["sex"]="man"
a["name"]="xixin"
print(a)
print(a['name'])
a["name"]="学习的机会"
a["class"]="moju092"
print("修改之后的字典值：{}".format(a))
print("字典里面的姓名是：{0}".format(a["name"]))
#删除字典元素
a.pop("age")
print("删除age之后的字典：{}".format(a))
print(a.keys())
print(a.values())
print(a.items())
c={"name":"伪证","age":"未知"}
a.update(c)
print(a)
print(a["score"][0])