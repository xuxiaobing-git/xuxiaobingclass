# -*- encoding: utf-8 -*-
"""
@File    : 福彩双色球.py
@Time    : 2020/11/22 13:58
@Author  : XuXiaoBing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
"""
1、“双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。
2、 红色球号码从1--33中选择；蓝色球号码从1--16中选择。
3、 选民手动输入号码
4、 选民可以复选或者依次选多张
5、 打印双色球显示结果，红球按顺序排序
6、 打印选中结果
7、举例说明：05、06、14、16、19、27、--10
"""
import random

double_balls = {'红球': [], '蓝球': []}  # 系统自动生成的票
reds = [i for i in range(1, 34)]  # 所有红球
blues = [i for i in range(1, 17)]  # 所有篮球
count = 0
num = 0
# 红球随机生成
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
print("红球：{} 蓝球：{}".format(red, blue))
# 清空
blue.pop(0)
for item in range(0, 6):
    red.pop(0)
print(double_balls)
