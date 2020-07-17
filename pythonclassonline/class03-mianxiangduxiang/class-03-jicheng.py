# -*- coding: utf-8 -*-
# @Time : 2020/7/16 22:02
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class-03-jicheng
# @Project : xuxiaobingclass
class BasePhone(object):
    """这是V1版本的手机：大哥大"""
    attr = "打电话"
    def call_phone(self):
        print("这个是打电话的功能")
    def func(self):
        print("大哥大的宁外一个功能当板砖用")
class NewPhone01(BasePhone):
    """这是V2版本的手机：老式手机"""
    def sendinfo(self):
        print("发送短信功能")
    def music(self):
        print("播放音乐")
    def func(self):
         # """第一种方式调用父类方法"""
        #BasePhone.func(self)
        super().func()
        """第二种方式调用父类方法"""
        print("这个手机很炫酷")
class NewPhone02(NewPhone01):
    """这是V3版本的手机：智能机"""
    def dispaly(self):
        print("播放视频")

#v1版本手机
v1 = BasePhone()

#v2版本手机
v2 = NewPhone01()
v2.func()
#v3版本手机
v3 = NewPhone02()