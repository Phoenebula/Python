#从1~n中，随机取m个数。1<=m<=n,数字不重复
#思路：建2个list，把n个数添加到第一个list，然后choice或者randint取数，取完从第一个list移除，把取出的数添加到第二个list
import  random
from random import randint
from random import choice
n = 34
m = 6

#用random.sample方法实现。range之前介绍过，可以产生一个序列。random.sample是从一个序列中随机取出一些元素。这正好满足了我们的要求。
list_m = random.sample(range(1, n), m)
list_n = randint(1,16)
print(list_m)
print(list_n)