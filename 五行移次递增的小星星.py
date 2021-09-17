# -*- coding: utf-8 -*-
# @File    : 五行移次递增的小星星.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/16 17:21
# @Function: b站黑马程序员视频P226-125 使用字符串直接输出小星星


row = 1
while row <= 5:
    print("*" * row)  # Python十分方便，可以直接用乘法进行循环打印
    row += 1