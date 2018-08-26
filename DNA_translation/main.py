#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

#fileName='dna.txt'
#inOBJ=open(fileName,'r')
#seq=inOBJ.read()
#Cleaning  new line and 
#seq=seq.replace('\n','')
#seq=seq.replace('\r','')

def translation(seq):
	'''
	This is a method that translates seq into code
	'''
	table = {
	    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
	    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}
	#print(table['ATA'])
	protein=''#lousy
	if len(seq)%3==0:
		#pass
		#print(seq[9:12])
		for i in range(0,len(seq),3):
			p_code=seq[i:i+3]
			protein+=table[p_code]
	#print(seq[6:9])
	return protein

def read_file(fileName):
	'''reads and returns the input sequence with special characters.'''
	with open(fileName) as inOBJ:
		seq=inOBJ.read()
		seq=seq.replace('\n','')
		seq=seq.replace('\r','')
	return seq


def main():
	#print('SINCHIGUANO')
	grounth_true=read_file('protein.txt')
	#print(tmp)
	print('########################')
	dna=read_file('dna.txt')
	#print(dna)
	#print(len(dna)%3)# so no possible
	tmp_protein=translation(dna[20:935])
	print(tmp_protein)
	print('================')
	print(grounth_true)
	print('+++++++++++++++++++++++++')
	print(grounth_true==tmp_protein)
	print(translation(dna[20:938])[:-1] == translation(dna[20:935]))

if __name__=='__main__':
	main()



	'''
		print(translation(seq[0:9]))#["GCC"]
	mod=138 % 13
	print(mod)
	print('####################################')
	print(translation(seq[40:49]))
	print(seq[40:49])
	#print(help(translation))

	'''