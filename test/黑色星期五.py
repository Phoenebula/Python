#!/usr/bin/python
# -*- encoding:UTF-8-*-
# 每个日期可以转成8位数字，比如 2017年12月4日 对应的就是 20171204。小明发现，自己的生日转成8位数字后，8个数字都没有重复，而且自他出生之后到今天，再也没有这样的日子了。请问小明的生日是哪天？

from datetime import date
import random
import datetime

# today =date.today()
# print(today)

day = datetime.datetime.now()
print(day)
while True:
    day = day + datetime.timedelta(days = -1)   #当前时间前一天
    days = day.strftime('%Y%m%d')   #把当前时间按年月日格式化
    s = set(days)   #利用集合的去重功能
    if len(s) == 8:
        print(days)
        break


# def __dateTolist__(year,month,day):
#     day1 = date(year,month,day)
#     d = str(day1)
#     list = []
#     a = {}
#     for i in d:
#         list.append (i)
#     list.remove ('-')
#     list.remove ('-')
#     # return list
#     for j in list:
#         if list.count(j) == 1:
#             a[j] = list.count(j)
#             print(a)
#             #break
#
#
# # def __isRepeat__(list):
# #     for j in list:
# #         # a[j] = list.count (j)
# #         if list.count(j) > 1:
# #             # a[j] = list.count(j)
# #             return 'noRepeat'
# #     print('a')
#
# __dateTolist__(2017,1,12)
#
# # __isRepeat__(b)
