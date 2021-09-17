# -*- coding: utf-8 -*-
# @File    : 判断语句演练—判断年龄.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 18:08
# @Function: b站黑马程序员视频P184-083 if基础-判断年龄演练


age = int(input("请输入你的年龄:"))
if 0 <= age <= 120:
    if age >= 18:
        print("可以进网把嗨皮！")
    else:
        print("给我爬，好好学习")
else:
    print("年龄不合理，不给予判断")