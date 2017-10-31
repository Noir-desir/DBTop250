# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:56:00 2017

@author: Administrator
"""
import requests
import re



def get_url(page):
    url = 'https://movie.douban.com/top250?start='+str(page)+'&filter='
    response = requests.get(url)
    content = response.text
    return content

def parse_page(content):
    pattern = re.compile('<div class="item">.*?<em class="">(\d+)</em>'+
                     '.*?alt="(.*?)"'+
                     '.*?rating_num.*?average">(.*?)</span>',re.S)
    results = re.findall(pattern, content)
    for result in results:
        return result.__str__()

def write_to(result):
    with open('filename.txt', 'w') as fw:
        fw.write(result)
        fw.close
  
def main(page):
    spy = get_url(page)
    result = parse_page(spy)
    write_to(result)

    
if __name__ == '__main__':
    main(i*25 for i in range(10))

print('finished!')