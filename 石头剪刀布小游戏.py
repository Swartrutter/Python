# -*- coding: utf-8 -*-
# @File    : 石头剪刀布小游戏.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 18:57
# @Function: b站黑马程序员视频P208-107 电脑随机出拳


import random
player = int(input("请输入您要出的手势（1-石头，2-剪刀，3-布）："))
computer = random.randint(1,3)
print("电脑随机出的手势为：",end='')
print(computer)
if player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("玩家失败")