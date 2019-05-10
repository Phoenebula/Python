# coding:UTF-8
#仍然是设定某个文件夹，不同的是要再增加一个文本参数，然后列出这个文件夹（含所有子文件夹）里，所有文件内容包括这个搜索文本的文件。
import os
import fnmatch
import re

f = open('basic.py','r')
content = f.read()
print(content)
f.close()

# for root,dirs,files in os.walk('.',topdown=True):
#     for name in files:
#     #     print(os.path.join(root,name))    #输出文件和路径
#     # for name in dirs:
#     #     print(name)
#         filename = open(name,'r')
#         filecontext = filename.read()
#
#
#         # if 'list' in filecontext:
#         #     print(name)
#
#         if fnmatch.fnmatch(filename,'print'):       #找出后缀txt的文件
#             print(name)
#         filename.close ()