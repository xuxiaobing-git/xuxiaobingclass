# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 22:54
# @File    : cards_tools.py.py
# @Software: PyCharm
# 存储名片数据
card_list = []


def show_menu():
    # 显示功能菜单
    print("*" * 25)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("1.新建名片")
    print("2.查看全部名片")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 25)


def new_card():
    """新建名片"""
    print("_" * 25)
    print("新建名片")
    # 输入用户的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入手机号：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 定义一个字典来接收用户新建信息
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 追加到列表里面进行存储
    card_list.append(card_dict)
    # print(card_list)
    print("您已经成功添加{}的名片".format(name_str))


def show_all():
    """查询所有名片"""
    print("_" * 25)
    print("查询所有名片")
    if len(card_list) == 0:
        print("当前无任何人名片")
        return
    # 打印表头
    for name in ["姓名", "手机号", "QQ号码", "邮箱"]:
        print(name, end="\t\t\t")
    print(" ")
    print("="*60)
    # 输出具体的名片信息
    for card_dict in card_list:
        print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))


def search_card():
    """查询单个名片"""
    print("_" * 25)
    print("查询单个名片")
