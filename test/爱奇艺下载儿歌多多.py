# -*-coding=utf-8-*-
# 儿歌多多在爱奇艺的视频网站上也有全集，所以目标转为抓取iqiyi的儿歌多多视频列表。
# github上有一个现成的下载iqiyi的第三方库，可以通过python调用这个库来实现下载功能。

import requests
import subprocess
from lxml import etree

session = requests.session()

def getContent(url):
    # url = "http://www.iqiyi.com/v_19rrkwcx6w.html"
    try:
        ret = session.get(url)
    except:
        return None
    if ret.status_code==200:
        return ret.text
    else:
        return None

def getUrl():
    url = "http://www.iqiyi.com/v_19rrkwcx6w.html"

    content = getContent(url)
    # content = content.decode('utf-8')
    # print(content)
    root = etree.HTML(content)
    elements = root.xpath('//script[@id]')
    # // div[ @ data - current - count = "1"] // li / a / @ href
    print(elements)
    # for items in elements:
    #     song_url = items.replace ('//', '')
    #     song_url = song_url.strip ()
    #     print (song_url)qdsszx

getUrl()