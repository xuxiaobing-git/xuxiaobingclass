# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 20:30
# @File    : 选彩票.py
# @Software: PyCharm
import random

double_balls = {'红球': [], '蓝球': []}  # 系统自动生成的票
reds = [i for i in range(1, 34)]  # 所有红球
blues = [i for i in range(1, 17)]  # 所有篮球
num = input("你要选多少注彩票？")
num = int(num)
p = 1
while p <= num:
    count = 0
    while count < 6:
        red_ball = random.choice(reds)  # 随机选取红球中的一个数
        if red_ball in double_balls["红球"]:
            continue
        else:
            double_balls["红球"].append(red_ball)
            count += 1
    # 篮球随机生成
    blue_ball = random.choice(blues)
    double_balls["蓝球"].append(blue_ball)
    # 红球升序排列
    red = double_balls['红球']
    red.sort()
    blue = double_balls["蓝球"]
    print("红球：{}   蓝球：{}".format(red, blue))
    # 清空
    blue.pop(0)
    for item in range(0, 6):
        red.pop(0)
    # print(double_balls)
    p += 1
