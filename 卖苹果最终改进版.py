# -*- coding: utf-8 -*-
# @File    : 卖苹果最终改进版.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 15:22
# @Function:


price = float(input("请输入苹果的单价："))
weight = float(input("请输入苹果的重量："))
print("苹果最终的价格为：",end='') #不让print换行
print(price * weight)