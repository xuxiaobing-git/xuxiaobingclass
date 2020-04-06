# -*- coding: utf-8 -*-
# @Time : 2020/4/6 18:20
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_10_02.py
# @Project : xuxiaobingclass
class  Boyfriend:
    height=175
    money=200000
    name="周杰伦"
    age=28
    @classmethod  #类方法
    def  cooking(cls):
        print("会做饭")
    @staticmethod # 静态方法
    def  hiking():
         print("喜欢户外运动")
#实例方法
    def  swimming(self):
        print(self.name+"喜欢游泳")
    def coding(self,language):
        print("会写{0}代码".format(language))

bf=Boyfriend()
bf.swimming()
bf.coding("python")
#实例方法
#如果是调用类里面的属性  self.属性名
#如果是实例方法自己带参数    参数传递的规则 同普通函数
