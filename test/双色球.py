#从1~n中，随机取m个数。1<=m<=n,数字不重复
#思路：建2个list，把n个数添加到第一个list，然后choice或者randint取数，取完从第一个list移除，把取出的数添加到第二个list
import  random
from random import choice
n = 10
m = 5

#用random.sample方法实现。range之前介绍过，可以产生一个序列。random.sample是从一个序列中随机取出一些元素。这正好满足了我们的要求。
list_m = random.sample(range(1, n), m)
print(list_m)

#用list方法实现
# list_n = []     #n个数的list
# list_get = []      #取出数的list
# for i in range(1,n+1):      #把1-n添加到list
#     list_n.append(i)
# print(list_n)
#
# for i in range(1,m+1):
#     #print(i)
#     #j = randint(1,n)        #用randint从list取数，但是有时候有报错，j超出list范围，不如choise好
#     j = choice (list_n)     #用choice从list取数，同上，2选1即可
#     #print (j)
#     list_get.append(j)      #把取出的数添加到另一个list
#     list_n.remove(j)        #从原来list移除取出的数
#     #print (list_n)
# print (list_n)
# print(list_get)

#用集合方法实现
def m_n():
    print ("本程序会从1～n中随机取m个数，1<=m<=n")
    # n = int(input("输入n的值："))
    # m = int(input("输入m的值："))
    random_num = set ()     #创建集合
    if 1 <= m <= n:
        while len (random_num) != m:
            random_num.add (random.randint (1, n))
        print (random_num)
    else:
        print ("=" * 40)
        print ('请确认1<=m<=n')
        print ('=' * 40)
        m_n ()
m_n ()
