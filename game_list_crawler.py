#@uncle nought
# -*- coding:utf-8 -*-

import os
import sys
import re
import random

input_filename = sys.argv[1] # 输入文件，使用方法 python game_list_crawler.py htmlcode.txt
output_filename = 'mysql_'+ input_filename # 输出文件是以空格为分隔符的txt，可以导入到mysql里面
input_file = open(input_filename)
output_file = open(output_filename, 'w')
content = input_file.read(); # read all content of html

# 因为html中要提取出来的游戏是一个列表<li>，因此需要把每一个<li>标签中的item都提取出来，得到一个items数组
p = re.compile(r'(<li class="item">)(.*?)(</li>)', re.DOTALL) # re.DOTALL匹配多行

# 下面几个pattern，都是用来匹配一个item中的各个标签
# (.*?)可以匹配出任意一段文本，()内表示是的一个group
p_name = re.compile(r'<span class="title">(.*?)</span>', re.DOTALL) 
p_type = re.compile(r'<span class="mark .*?">(.*?)</span>', re.DOTALL) 
p_imgurl = re.compile(r'<img xSrc="(.*?)"(.*?)', re.DOTALL)
p_gameurl = re.compile(r'<a href="(.*?)" class="clearfix".*?>', re.DOTALL)

for m in p.finditer(content):
    line = m.group(2)
    # search name
    game_name = p_name.search(line).group(1)
    # search type
    game_type = p_type.search(line).group(1)
    game_type = game_type + '小游戏'
    # search imgurl
    game_imgurl = p_imgurl.search(line).group(1)
    # search gameurl
    game_url = p_gameurl.search(line).group(1)
    # add some args
    update_time = '2014-9-28' # new date
    rate = '5'
    description = '马上来玩小游戏' + game_name + '吧~'
    popularity = str(random.randint(123456, 999999)) # random a popularity
    #print update_time
    #print rate
    #print description
    #print popularity + '\n\n'
    output_line = game_name + ' ' + game_type + ' ' + update_time + ' ' +  rate + ' ' + popularity + ' ' + game_imgurl + ' ' + game_url + ' ' + description + '\n'
    print output_line
    output_file.write(output_line)

input_file.close()
output_file.close()

