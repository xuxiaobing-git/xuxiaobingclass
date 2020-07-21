# -*- coding: utf-8 -*-
# @Time : 2020/7/17 21:29
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class-004-attrset
# @Project : xuxiaobingclass

class TestCases(object):
    def __init__(self,url,data,excepted,actual):
        self.url=url
        self.data=data
        self.excepted=excepted
        self.actual=actual

case1= TestCases(url="www.baidu.com", data={"user":999}, excepted={"user":11}, actual={"code":11})
setattr(case1,"method","post")
res = getattr(case1,"method")
print(res)