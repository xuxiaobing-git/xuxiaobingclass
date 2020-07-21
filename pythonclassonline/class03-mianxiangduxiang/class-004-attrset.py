# -*- coding: utf-8 -*-
# @Time : 2020/7/17 21:29
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class-004-attrset
# @Project : xuxiaobingclass


#定义测试类
class TestCases(object):
    def __init__(self,url,data,excepted,actual): #初始化属性
        self.url=url
        self.data=data
        self.excepted=excepted
        self.actual=actual
#创建一个对象
case1= TestCases(url="www.baidu.com", data={"user":999}, excepted={"user":11}, actual={"code":11})
#利用反射机制操作对象属性
#设置属性
setattr(case1,"method","post")
#获取属性
res = getattr(case1,"method")
print(res)
#删除属性
#delattr(case1,"url")
print(case1.url)