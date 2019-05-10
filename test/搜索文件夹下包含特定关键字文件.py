# coding:UTF-8
#仍然是设定某个文件夹，不同的是要再增加一个文本参数，然后列出这个文件夹（含所有子文件夹）里，所有文件内容包括这个搜索文本的文件。
import os
import fnmatch
import re

key = 'aa'
#root = "C:\Python\test\test1"
list = []
for root,dirs,files in os.walk('.'):
    for name in files:
       list.append(os.path.join (root,name))
       print (list)
       #  filename = open(name,'r')
       #  filecontext = filename.read()
       #  # if filecontext.find('100'):
       #  #     list.append(os.path.join(root,name))
       #  if re.search('100',filecontext):
       #      print(name)
        # # if os.path.splitext (filename)[1] == '.py':
        # #     content = open (os.path.join (root, filename), 'r').read ()
        # #     if re.search ('import os', content):

        #print(name)
        # filename.close ()
