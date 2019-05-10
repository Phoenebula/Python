#字符串取出数字，将其输出成新字符串
import re
text_origin ='aAsmr3idd4bgs7Dlsf9eAF'
find = r'[0-9]'
#find = r'\bs\S*?e\b'
text_number = re.findall(find,text_origin)
print(text_number)
text_new = ''.join(text_number)
print(text_new)

#
# 上一个坑，取出字符串中的数字，在论坛上出现了好几种方法。除了基本的遍历判断来做外，还有一些简便的python解法：
# 1.正则
# ''.join(re.findall(r'[\d|.]+',text))
#
# 2.isdigit
# ''.join([i for i in text if i.isdigit()])
# [i for i in test]这是一种生成list的方法，通过后面的if可以增加生成时的过滤条件。这种写法在python中很常用。
#
# 3.filter
# filter(lambda x: x.isdigit(), text)
# filter是一个过滤器，其中的lambda表达式是过滤的条件。这个稍微高深了一点，有兴趣的同学可以去搜索一下“lambda表达式”。