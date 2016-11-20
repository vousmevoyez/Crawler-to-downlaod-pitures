# -*- coding: utf-8 -*-
import urllib
import re
import math

count = 0
# get all links in the page
url = urllib.urlopen('http://www.meitulu.com/search/%E6%9F%B3%E4%BE%91%E7%BB%AE').read()
pp1 = r'"http://www.meitulu.com/item/.+?.html"'
ppp1 = re.compile(pp1)
url_list = re.findall(ppp1,url)
new_url_list = []
index = 0
while index <= len(url_list)-1:
	new_url_list.append(url_list[index][1:-1])
	index += 2


for id in range(len(new_url_list)):
	# get how many pages there are in each link
	url1 = urllib.urlopen(new_url_list[id]).read()
	pp2 = r'<a href="http://www.meitulu.com/item/\d{4}\_\d{1,2}.html">\d{1,2}'
	ppp2 = re.compile(pp2)
	num_of_pages = re.findall(pp2,url1)
	special_index = num_of_pages[-1].index('>')
	n_pages = int(num_of_pages[-1][special_index+1:])
	# 下载
	for i in range(n_pages):
		address = new_url_list[id]
		if i != 0:
			address = address[:-5] + '_' + str(i) + '.html'
		url = urllib.urlopen(address).read()
		pp3 = r'img src=(http://.+?jpg) ' 
		ppp3 = re.compile(pp3)
		img = re.findall(ppp3,url)
		for imgurl in img:
			# You should change to your directory
			filename = 'C:\\Users\\KrystalU\\Desktop\\lyq1\\' + str(count) + '.jpg'  
			urllib.urlretrieve(imgurl,filename)
			count += 1
