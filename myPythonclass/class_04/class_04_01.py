# -*- coding: utf-8 -*-
# @Time : 2019/11/30 13:51
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_04_01.py
# @Project : xuxiaobingclass
a=[1,0.05,"lemonban",(1,2,3),[4,5,6]]
#新增一个元素
#append 加载列表的最后,每次只能添加一个元素
a.append("冷萌")
print(a)
#insert（）添加元素到列表指定位置
a.insert(0,"许小兵")
print(a)
#修改列表的值
a[-1]="我要学Python"
print(a)
