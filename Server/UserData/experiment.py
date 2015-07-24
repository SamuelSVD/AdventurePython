#!/usr/bin/env python
try:
	users = {}
	file = open('accounts.txt', 'r')
	list = file.read()
	file.close()
	list = list.split('\n')
	for line in list:
		line = line.split()
		users[line[0]] = line[1]
	print users
except:
	print 'lol'
file = open('accounts.txt', 'a')
file.write('\nSam Vergara')
file.close()	