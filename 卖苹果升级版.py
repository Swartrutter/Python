# -*- coding: utf-8 -*-
# @File    : 卖苹果升级版.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 14:21
# @Function: b站黑马程序员视频P169-069 买苹果增强版演练


price_str = input("请输入苹果的价格：")
weight_str = input("请输入苹果的重量:")
# 通过input()函数的官方解释，从标准输入读取一个字符串。所以，输入的内容的数据类型应该是字符串类型。

# 验证如下：
print(type(price_str))
print(type(weight_str))
# 验证结束。

price = float(price_str)
weight = float(weight_str) #将str类型的数据转换成为浮点类型,因为str字符串类型数据不能进行计算
money = price * weight
print("苹果的最终价格为:",end='')  #若不想让print换行则需要在末尾加上 ,end=''
print(money)