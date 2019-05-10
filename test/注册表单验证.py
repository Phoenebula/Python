#!/usr/bin/python
# -*- encoding:UTF-8-*-
text ='静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。'
list_origin = []
current = []
m = 6
n = int(len(text)/m)
for b in text:
    list.append(b)
# print(list)

for i in range(0,n ):
    c = list[0:m]
    del (list[0:m])
    current.append (c)
print (current)
print (list)
