# -*- coding: utf-8 -*-
# @File    : Wordgame_1.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 12:52
# @Function: b站小甲鱼视频：002用Python设计第一个游戏

guess = int(input("猜猜我现在心里在想的数字是什么：")) #将标准输入的字符串类型数据强制转化为整型
if guess == 8:
    print("666这都给你猜中了")
    print("但是猜中了也没啥用")
else:
    print("这你都猜不中，太让我失望了")
print("游戏只有一次机会噢，不玩啦！")