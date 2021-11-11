# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 22:53
# @File    : cards_main.py.py
# @Software: PyCharm

import 名片管理系统.cards_tools

while True:
    # 显示功能菜单
    名片管理系统.cards_tools.show_menu()
    action_str = input("请选择希望执行的操作:")
    print("您选择的操作是【{}】".format(action_str))
    #   输入1 2 3表示正确选择操作指令
    if action_str in ["1", "2", "3"]:
        # 新建名片
        if action_str == "1":
            pass
        # 查看全部名片
        elif action_str == "2":
            pass
        # 查询名片
        elif action_str == "3":
            pass
    #   输入0表示退出系统
    elif action_str == "0":
        print("您已退出系统，欢迎下次使用")
        break
    #   输入其他内容提示输入错误，需要提示用户
    else:
        print("您输入的有误，请重新输入")
