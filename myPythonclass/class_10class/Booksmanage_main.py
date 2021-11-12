# -*- encoding: utf-8 -*-
"""
@File    : Booksmanage_main.py
@Time    : 2020/6/21 11:25
@Author  : xuxiaobing
@Email   : 676308756@qq.com
@Software: PyCharm
"""
import class_10class.Booksmanage_tools

# books = [{"id": "1", "name": "天龙八部", "position": "A01-01B-01"},
#          {"id": "2", "name": "水浒传", "position": "A01-01B-02"},
#          {"id": "3", "name": "西游记", "position": "A01-01B-03"},
#          {"id": "4", "name": "红楼梦", "position": "A01-01B-04"},
#          {"id": "5", "name": "三国演义", "position": "A01-01B-05"}]

class_10class.Booksmanage_tools.read_data()
print("~~~~~~~欢迎使用图书管理系统~~~~~~~")
while True:
    class_10class.Booksmanage_tools.print_menu()  # 打印菜单
    num = input("请输入您的选项")
    if num == "1":
        class_10class.Booksmanage_tools.add_book()  # 添加图书
    elif num == "2":
        class_10class.Booksmanage_tools.del_book()  # 删除图书
    elif num == "3":
        class_10class.Booksmanage_tools.all_book()  # 显示所有图书
    elif num == "4":
        # 退出程序
        print("谢谢使用，程序即将关闭")
        break
    else:
        print("您选择的有误，请重新选择")
class_10class.Booksmanage_tools.write_data()
