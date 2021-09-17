# -*- coding: utf-8 -*-
# @File    : 格式化输出基本练习.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 17:30
# @Function: b站黑马程序员视频P173-074 变量的输入输出-格式化输出基本练习


name = "小明"
print("我的名字叫 %s,请多多关照" % name)

student_no = 1
print("我的学号是 %06d" % student_no) # %06d表示输出显示一共六位的整数，不足位数的用0补齐

price = 9.00
weight = 5.00
money = 45.00
print("苹果单价 %0.2f元/斤，购买了 %0.2f斤，需要支付%0.2f元" % (price , weight , money)) # %0.2f表示输出显示小数点后两位

scale = 10.00
print("数据比例是 %0.2f%%" % scale)