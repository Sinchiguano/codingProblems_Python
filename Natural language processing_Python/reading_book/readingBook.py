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


title='shakespeare.txt'

def readBook(title_path):
	'''
	Read a book and return it as a string.
	'''
	with open(title_path,'r') as file:
		txt=file.read()
		txt=txt.replace('\n','').replace('\r','')
	return txt


def main():
	print('Cesar SINCHIGUANO')

	txt=readBook(title)
	#print(len(txt))
	aux='The King is kind'
	index=txt.find(aux)
	print(index)
	#index: 1307581

	sample=txt[index:index+100]#
	print(sample)


if __name__=='__main__':
	main()