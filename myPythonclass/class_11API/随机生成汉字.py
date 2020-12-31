# -*- encoding: utf-8 -*-
"""
@File    : 随机生成汉字.py
@Time    : 2020/12/31 11:09
@Author  : XuXiaoBing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
import random

num = input("请输入随机输出多少汉字：")
num = int(num)
p = 1


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str


if __name__ == '__main__':
    while p <= num:
        print(Unicode(), end="")
        # print(GBK2312())
        p += 1
