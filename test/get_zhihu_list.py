import time
import re
import os
import requests
from bs4 import BeautifulSoup

def get_list():
    url = 'https://www.zhihu.com/api/v4/columns/crossin/articles?include=data[*].topics&limit=10'
    article_dict = {}

    resp = requests.get (url, headers=headers)
    j = resp.json ()
    data = j['data']


    # while True:
    #     print('fetching', url)
    #     try:
    #         resp = requests.get(url, headers=headers)
    #         j = resp.json()
    #         data = j['data']
    #     except:
    #         print('get list failed')

    for article in data:
        aid = article['id']
        akeys = article_dict.keys()
        if aid not in akeys:
            article_dict[aid] = article['title']
    with open('zhihu_ids.txt', 'w',encoding='utf-8') as f:
        items = sorted(article_dict.items())
        for item in items:
            print(item)
            f.write('%s %s\n' % item)
        # if j['paging']['is_end']:
        #     break
        # url = j['paging']['next']
        # time.sleep(2)

headers = {
        'origin': 'https://zhuanlan.zhihu.com',
        'referer': 'https://zhuanlan.zhihu.com/crossin' ,
        'User-Agent': ('Mozilla/5.0'),
    }
s=get_list()
print(s)
