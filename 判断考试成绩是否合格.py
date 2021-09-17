# -*- coding: utf-8 -*-
# @File    : 判断考试成绩是否合格.py
# @Author  : Swartrutter_
# @IDE     : PyCharm
# @Time    : 2021/1/15 18:38
# @Function: b站黑马程序员视频P194-093 考试成绩的判断


python_score = int(input("请输入你的python课程考试成绩："))
c_score = int(input("请输入你的c课程考试成绩："))
if python_score and c_score >= 90:
    print("优秀！")
elif python_score and c_score >= 80:
    print("良好")
elif python_score or c_score >= 60:
    print("考试通过")
else:
    print("考试不通过")
