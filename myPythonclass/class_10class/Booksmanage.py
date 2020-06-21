# -*- encoding: utf-8 -*-
"""
@File    : Booksmanage.py
@Time    : 2020/6/21 11:25
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""


def print_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("【1】：添加图书")
    print("【2】：删除图书")
    print("【3】：显示所有图书")
    print("【4】：退出")


def add_book():

# def del_book():
# def all_book():


def main2():
    print("~~~~~~~欢迎使用图书管理系统~~~~~~~")
    while True:
        print_menu()  # 打印菜单
        num = input("请输入您的选项")
        if num == "1":
            add_book() # 添加图书
        elif num == "2":
            del_book()  # 删除图书
        elif num == "3":
            all_book()  # 显示所有图书
        elif num == "4":
            # 退出程序
            print("谢谢使用，程序即将关闭")
            break


main2()
