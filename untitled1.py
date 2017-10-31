# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:31:21 2017

@author: Administrator
"""

import requests
import re

#f = open('C:/Users/Administrator/Desktop/1.txt','r+',encoding='utf-8')
#content = f.read()

response = requests.get('https://movie.douban.com/top250?start=0&filter=')
content = response.text

pattern = re.compile('<div class="item">.*?<em class="">(\d+)</em>'+
                     '.*?alt="(.*?)"'+
                     '.*?rating_num.*?average">(.*?)</span>',re.S)
results = re.findall(pattern, content)
result_list = []
for i in results:
    n=' '.join(i)
    result_list.append(n)
result = '\n'.join(result_list)
    