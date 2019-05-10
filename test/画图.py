#!/usr/bin/python
# -*- encoding:UTF-8-*-
# 如果一个正整数等于其各个数字的立方和，则称该数为阿姆斯特朗数（亦称为自恋数、自幂数）。
# 如 407 = 43 + 03 + 73 就是一个阿姆斯特朗数。
# 写一段代码，输出 1000 以内的所有阿姆斯特朗数。
import math

#数字拆分，如123拆分成1,2,3,并计算立方
def __chaifen__(n):
    l = list(str(n))
    mi = 0
    for i in range(0,len(l)):
        mi = mi + int(l[i])**3
    return (mi)

for i in range(0,1000):
    if i == __chaifen__(i):
        print(i)

# print(__chaifen__(99))