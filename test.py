# @uncle nought
# -*- coding:utf-8 -*-
import urllib2
import time
import re
import random

# 初始化的参数,url,页码,总页码,日期等
url = "http://h.7k7k.com/pc/"
page = 2
total_page = 10
date = time.strftime("%Y-%m-%d", time.localtime()) 
out_filename = "game-resource-" + date + ".csv"
output_file = open(out_filename, 'w')

# 定义类和各个属性的patterns, 游戏名称、链接、缩略图采用实际抓取，其他采用随机生成
p = re.compile(r'(<div class="game-item">)(.*?)(开始游戏</a></div>)', re.DOTALL) # re.DOTALL匹配多行
p_name = re.compile(r'<p class="title">(.*?)</p>', re.DOTALL)
p_imgurl = re.compile(r'<div class="pic"><img src="(.*?)" alt=""></div>', re.DOTALL)
p_gameurl = re.compile(r'<a href="(.*?)" target="_blank">', re.DOTALL)

while (page <= total_page):
	print "正在抓取第" + str(page) + "页资源...\n"
	print "名称\t" + "类型\t" + "更新日期\t" + "游戏评分\t" + "人气\t" + "截图地址\t" + "游戏地址\t" + "游戏描述" 
	response = urllib2.urlopen(url + str(page))
	html = response.read()
	page += 1
	# print html
	# 首先匹配出每一条游戏的item，接着提取每个游戏的属性
	for m in p.finditer(html):
		item = m.group(2)
		# print item + "\n"
		game_name = p_name.search(item).group(1)
		game_name = "".join(game_name.split())  # 去除name中间的空格
		game_img = p_imgurl.search(item).group(1)
		game_url = p_gameurl.search(item).group(1)
		game_type = "休闲小游戏"
		game_rate = str(random.randint(3, 5))
		game_popularity = str(random.randint(111111, 999999))
		game_desc = "超级好玩的小游戏" + game_name + "!"
		output_line = game_name + ' ' + game_type + ' ' + date + ' ' +  game_rate + ' ' + game_popularity + ' ' + game_img + ' ' + game_url + ' ' + game_desc + '\n'
		print output_line
		output_file.write(output_line)

output_file.close()