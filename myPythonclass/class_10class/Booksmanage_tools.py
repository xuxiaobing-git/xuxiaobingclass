# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 23:16
# @File    : Booksmanage_tools.py.py
# @Software: PyCharm
import time
import os

books = []  # 初始化变量


def read_data():
    if os.path.exists("books.txt"):
        with open("books.txt", "r", encoding="utf8") as f:
            cases = f.readlines()
        for case in cases:
            case = case.replace("\n", "")
            DaTas = case.split("，")
            dic = {}
            for i in DaTas:
                data = i.split("：")
                dic[data[0]] = data[1]
            books.append(dic)
    else:
        print("系统暂无书籍")


def write_data():
    if os.path.exists("books.txt"):
        os.remove("books.txt")
    for i in books:
        newBook = ("id：{}，name：{}，position：{}".format(i["id"], i["name"], i["position"]))
        with open("books.txt", "a", encoding="utf8") as f:
            f.write(str(newBook + '\n'))


def print_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("【1】：添加图书")
    print("【2】：删除图书")
    print("【3】：显示所有图书")
    print("【4】：退出")


def add_book():
    new_book = {}  # 创建字典存储图书编号
    while True:
        new_book["id"] = input("请输入图书编号")
        for book in books:  # 遍历所有图书，判断编号是否重复
            if book["id"] == new_book["id"]:
                print("已有图书：{}".format(book))
                print("图书编号不能重复")
                break
        else:  # 上述for循环 没找到重复的id   进入else
            new_book["name"] = input("请输入书名：")
            new_book["position"] = input("请输入书籍位置")
            books.append(new_book)
            print("添加成功")
            break

        time.sleep(2)


def del_book():  # 删除书籍
    book_name = input("请输入你要删除的书籍")
    find_list = []  # 创建一个空列表存储书籍
    for book in books:  # 遍历所有书籍，查找是否有该书籍
        if book_name == book["name"]:
            find_list.append(book)

    if len(find_list) != 0:  # 判断接收的列表是否为空，如果为空说明没有改数据
        print("一共找到{}本同名书籍,名为：{}".format(len(find_list), book["name"]))
        for book in find_list:
            print("编号:{}， 书名：{}，位置：{}".format(book["id"], book["name"], book["position"]))
        id_num = input("请输入你要删除的书籍编号：")
        # 根据书籍编号进行删除书籍,
        for book in find_list:
            if id_num == book["id"]:
                books.remove(book)
                print("删除成功")
                break
            else:
                print("输入的编号有误")
    else:
        print("抱歉没有该书籍")
    time.sleep(2)


def all_book():
    book_count = len(books)
    if book_count == 0:
        print("当前系统没有任何书籍，返回菜单主页")
    else:  # 显示当前所有书籍
        print("当前共有{}本书籍，所有书籍详细信息如下所示".format(book_count))
        for book in books:
            print("编号：{}， 书名：{}， 位置：{}".format(book["id"], book["name"], book["position"]))
        print("查询完毕，返回主菜单")
    time.sleep(2)
