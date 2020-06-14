# -*- encoding: utf-8 -*-
"""
@File    : class_lianxi_iforwhile.py
@Time    : 2020/6/14 10:09
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
# 商品折扣的案例，此处没有考虑金额为小数的情况，有待优化
import random

Money = int(input("请输入购买金额："))
if 0 < Money < 50:
    print("您的购买无折扣")
elif 50 <= Money <= 100:
    print("折扣为10%，您需要支付{}元".format(Money - Money * 0.1))
elif Money > 100:
    print("折扣为20%，您需要支付{}元".format(Money - Money * 0.2))
else:
    print("您输入的金额有误")
# 判断输入的字符是不是回文数
Num_str = input("输入五位数字：")
if Num_str[0] == Num_str[-1] and Num_str[1] == Num_str[-2]:
    print("此数字为回文数{}".format(Num_str))
else:
    print("不是回文数")
# 1-10随机生成一个数比较大小
n = random.randint(1, 9)
print(n)
My_num = int(input("请输入一个个位数"))
if My_num < n:
    print("小于随机数")
elif My_num > n:
    print("大于随机数")
else:
    print("等于随机数")


