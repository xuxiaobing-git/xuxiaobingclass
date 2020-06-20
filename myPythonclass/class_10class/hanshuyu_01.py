# -*- coding: utf-8 -*-
# @Time : 2020/6/20 20:06
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : hanshuyu_01
# @Project : xuxiaobingclass

num = 1000
def func1():
    print("func1---num",num)

    def func3():
        global num
        num+=1
        print("func3---num",num)
    func3()
    print("func1-02--num",num)

func1()
print(num)


