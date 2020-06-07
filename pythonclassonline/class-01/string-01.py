# -*- coding: utf-8 -*-
# @Time : 2020/6/2 22:18
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : string-01
# @Project : xuxiaobingclass

# str1 = "python1"
# str2 = "python2"
# str5 = str1 + str2
# str6 = str2.split("y")
# print(str5)
# print(str6)
# str2 ="aa bb c  7  jj  aa  ll"
# res1 = str2.split(" ")
# print(res1)
# res2="".join(res1)
# print(res2)
# print(res2.upper())

# str4 = "今天收来{}，交来学费{:.2f}，日期{}"
# print(str4.format("小明",8000, "2020606"))
name = "小明"
age = 18
money = 99.09
str1 = "这位同学{}，今年{}，银行卡余额{}"
print(str1.format(name , age , money))
print ("{} 对应的位置是 {{0}}".format("runoob"))
"""
3.1415926	    {:.2f}	    3.14	    保留小数点后两位
3.1415926	    {:+.2f}	    +3.14	    带符号保留小数点后两位
-1	            {:+.2f}	    -1.00	    带符号保留小数点后两位
2.71828	        {:.0f}	    3	        不带小数
5	            {:0>2d}	    05	        数字补零 (填充左边, 宽度为2)
5	            {:x<4d}	    5xxx	    数字补x (填充右边, 宽度为4)
10	            {:x<4d}	    10xx	    数字补x (填充右边, 宽度为4)
1000000	        {:,}	    1,000,000	以逗号分隔的数字格式
0.25	        {:.2%}	    25.00%	    百分比格式
1000000000	    {:.2e}	    1.00e+09	指数记法
13	            {:>10d}	    13	        右对齐 (默认, 宽度为10)
13	            {:<10d}	    13	        左对齐 (宽度为10)
13	            {:^10d}	    13	        中间对齐 (宽度为10)
11	进制 :
            '{:b}'.format(11)   1011
            '{:d}'.format(11)   11
            '{:o}'.format(11)   13
            '{:x}'.format(11)   b
            '{:#x}'.format(11)  0xb
            '{:#X}'.format(11)  0XB	
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
b、d、o、x 分别是二进制、十进制、八进制、十六进制          





"""