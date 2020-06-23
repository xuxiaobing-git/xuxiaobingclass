# -*- encoding: utf-8 -*-
"""
@File    : carID.py
@Time    : 2020/6/23 15:25
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
import random
seed = "1234567890"
sa = []
for c in range(5):
    sa.append(random.choice(seed))
new_plateNumber = "晋A" + "".join(sa)
print(new_plateNumber)
