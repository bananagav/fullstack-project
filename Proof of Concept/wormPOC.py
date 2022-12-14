#!/usr/bin/env python3

from sys import argv
import os

script = argv
name = str(script[0])

cmd = 'cat payload.txt'
os.system(cmd)
if os.path.exists('clone'):
	os.system(r'rm -r clone')
os.mkdir('clone')
os.system(r"cp payload.txt clone")
os.system(r"cp " + name + " clone")

