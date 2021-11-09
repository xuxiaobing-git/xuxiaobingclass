# -*- encoding: utf-8 -*-
"""
@File    : file_write.py
@Time    : 2020/6/21 15:49
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
import os
books = [{'id': '1', 'name': '天龙八部', 'position': 'A01-01B-01'},
         {'id': '2', 'name': '水浒传', 'position': 'A01-01B-02'},
         {'id': '3', 'name': '西游记', 'position': 'A01-01B-03'},
         {'id': '4', 'name': '红楼梦', 'position': 'A01-01B-04'},
         {'id': '5', 'name': '三国演义', 'position': 'A01-01B-05'},
         {'id': '09', 'name': 'kkk33', 'position': 'kkk///'}]

if os.path.exists("books.txt"):
    os.remove("books.txt")
for i in books:
    newBook = ("id：{}，name：{}，position：{}".format(i["id"], i["name"], i["position"]))
    with open("books.txt", "a", encoding="utf8") as f:
        f.write(str(newBook + '\n'))
