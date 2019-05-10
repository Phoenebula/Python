#!/usr/bin/python
# -*- encoding:UTF-8-*-
# 用一段代码来压缩图片大小。提示，可以使用 Pillow 库来解决。
# 实现单张图片的压缩不难，所以附加题，将这段代码制作成一个命令行工具，使其可以：
# 指定要压缩的图片文件
# 如果指定的是一个目录，则压缩整个目录里的图片
# 指定压缩的比率
# 指定输出的文件路径
# 选择是否保留原始图片
# 推荐使用 argparse 模块实现。
import argparse
import os
from PIL import Image

#获取参数
parser = argparse.ArgumentParser(description='批量压缩保存图片')

help_pic_addr = '某张图片地址或者某个文件夹地址：支持相对地址和绝对地址'
parser.add_argument('--addr',type=str,help=help_pic_addr,default=None)
args = parser.parse_args()

#判断地址里文件能否打开
def is_img(addr):
    #尝试打开该地址
    #不能被打开可能数路径错误或者文件类型错误
    try:
        im = Image.open(addr)
        return True
    except Exception as e:
        print('处理{}文件时发生错误，已经跳过该文件'.format(addr))
        return False

#获取文件路径
def get_pics_from_dir(path):
    #遍历指定文件夹
    #将所有图片地址添加到列表res
    res = []
    for root,dirs,files in os.walk(path):
        for f in files:
            addr = os.path.join(root,f)     #获取该路径的文件,如c:/test/test.jpg
            if is_img(addr):
                res.append(addr)        #如果该路径文件能被打开，则把该路径文件添加到列表
    return res

help_ratio = 0.5
path =r'C:/Python/test/charpg/'
c = get_pics_from_dir(path)
for file in c:
    #print(file)
    im = Image.open(file)
    weight,height = im.size
    w = int(weight*help_ratio)
    h = int(height*help_ratio)
    reIm = im.resize((w,h))
    name = file.split('/')[-1]  #将file按/分割，最后一个元素是xx.jpg，它是list的[-1]，list[0]是第一个元素。
    # print(name)
    #查看目的文件夹是否已经存在该文件名，如果存在则在前面添加_
    # file_path = os.path.join(path,name)
    # while os.path.exists(file_path):
    #     name = '_'+name
    #     file_path = os.path.join(path,name)
    #     reIm.save(file_path)
    #     break
    while os.path.exists(file):
        name = '_'+name
        file = os.path.join(path,name)
        #file_path = os.path.join(path,name)
        reIm.save(file)
        break       #这里需要break，要不一直循环。
    print(file)
    print('文件{0}经处理后保存为{1}'.format(file,name))


    # reIm.save(r'C:\Python\test\charpg\snow1.jpg')