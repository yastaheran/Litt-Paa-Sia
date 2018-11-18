#!/usr/bin/env python

import sys, glob, os

def searchDir(str, dir):
	root = dir #startmappe
	for root, sub, files in os.walk("."):
		path = root.split(os.sep)
		print((len(path) - 1) * '---', os.path.basename(root))
		for fname in files:
			if str in fname:
				print(len(path) * '---', fname)

string = sys.argv[1]
directory = sys.argv[2]
searchDir(string, directory);

""" Går igjennom hele mappen
for root, subdir, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file) """