# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num = int(input())

for i in range(0, num):
	for j in range (num-(i+1)):
		print(' ',end='')
	for k in range(0, i+1):
		print('*',end='')
	print("")
	