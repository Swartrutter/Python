# -*- coding: utf-8 -*-
# @File    : 九九乘法表.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/16 17:32
# @Function: b站黑马程序员视频P230-129 九九乘法表


def multiple_table(): #已将下方代码封装到函数multiple_table()中
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d * %d = %d" % (j, i, j * i), end='')
            print("  ", end='')
            j += 1
        print()
        i += 1