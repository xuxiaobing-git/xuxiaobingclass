# -*- coding: utf-8 -*-
# @Time : 2020/6/22 22:14
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : readfile
# @Project : xuxiaobingclass
books = []
with open("case.txt","r",encoding="utf8") as f:
    cases = f.readlines()
for case in cases:
    case = case.replace("\n","")
    DataS = case.split(",")
    dic = {}
    for i in DataS:
        data = i.split(":")
        #print(data)
        dic[data[0]] = data[1]
    print(dic)
    books.append(dic)
print(books)
