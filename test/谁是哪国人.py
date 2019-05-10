#!/usr/bin/python
# -*- encoding:UTF-8-*-
# 找出一年中哪些日子是“黑色星期五”日期为13且为星期五的那天

from datetime import date
import random
import datetime


# day = datetime.datetime.now()
# days = day.strftime('%Y%m%d')
# # print(days)
# # s = days[-2:]        #截取日期最后2位
# # print(s)
# # w = day.weekday()   #返回给定日期是一周的第几天，星期一是0，星期日是6
# # print(w+1)
# while True:
#     day = day + datetime.timedelta(days = 1)   #当前时间后一天
#     days = day.strftime('%Y%m%d')   #把当前时间按年月日格式化
#     w = day.weekday ()  # 返回给定日期是一周的第几天，星期一是0，星期日是6
#     s = days[-2:]   #日期的日子，最后2位
#     if s == '13' and w ==4 :
#         print(days)
#         break

for i in range(1,13):
    d = date(2018,i,13)     #直接用date（年，月，日）
    w = d.weekday()
    if w == 4:
        print(d)