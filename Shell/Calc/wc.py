#!/usr/bin/env python

import sys, glob


fn = sys.argv[1]	#the filename

a = 0		#number of lines in file
b = 0		#number of words in file
c = 0		#number of characters in file


if fn == '*.py':
	for filename in glob.glob('*.py'): #eller for '*.py' in os.listdir(os.getcws()):
		file = open(filename, 'r')
		for line in file:
			words = line.split()
			a += 1
			b += len(words)
			c += len(line)
		print(a, b, c, filename)
		
elif fn == '*':
	for filename in glob.glob('*.txt'):
		file = open(filename, 'r')
		for line in file:
			words = line.split()
			a += 1
			b += len(words)
			c += len(line)
		print(a, b, c, filename)
else:
	file = open(fn, 'r')
	for line in file:
		words = line.split()
		a += 1
		b += len(words)
		c += len(line)

	print(a, b, c, fn)
