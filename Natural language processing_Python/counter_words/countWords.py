#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
from collections import Counter


txt='I am Cesar, alias Sinchiguano; I will keep this file simple:...'


'''
Count the number of times each word occurs in text (str). Return ditionary where the keys
are unique words and values are word counts.
'''

def counterWords1(txt):
	#print('CESAR SINCHIGUANO')
	tmp=dict()

	filter=['.',',',';',':']
	for i in filter:
		txt=txt.replace(i,'')

	aux=txt.split(" ")


	for item in aux:
		#print(item)
		if item in tmp:
			tmp[item]+=1
			#print('yes')
		else:
			tmp[item]=1
			#print('no')
	return tmp
def counterWords2(txt):

	filter=['.',',',';',':']
	for i in filter:
		txt=txt.replace(i,'')

	wordsCounts={}
	wordsCounts=Counter(txt.split(' '))
	return wordsCounts
def main():
	#print('Cesar SINCHIGUANO')

	print(counterWords1(txt))
	print(counterWords2(txt))
	print(counterWords1(txt)==counterWords2(txt))



if __name__=='__main__':
	main()