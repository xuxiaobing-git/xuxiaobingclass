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
    print("=" * 60)
    # 输出具体的名片信息
    for card_dict in card_list:
        print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))


def search_card():
    """查询单个名片"""
    print("_" * 25)
    find_name = input("请输入你要查找的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(card_dict["name"],
                                                      card_dict["phone"],
                                                      card_dict["qq"],
                                                      card_dict["email"]))
            deal_card(card_dict, find_name)
            break
    else:
        print("你查找的名片不存在")


def deal_card(find_dict, find_name):
    action_str = input("请选择你想要执行的操作："
                       "【1】修改名片 "
                       "【2】删除名片 "
                       "【0】返回上一级 :")
    if action_str == "1":
        print("开始修改名片")
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱")

        print("{}的名片修改成功".format(find_name))
    elif action_str == "2":
        card_list.remove(find_dict)
        print("已经成功删除{}名片".format(find_name))


def input_card_info(dict_value, tip_message):
    """
    用户修改名片时输入的信息
    :param dict_value:字典中原有的值
    :param tip_message:用户手动输入信息
    :return:如果用户输入了内容就返回输入内容，否则则使用原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
