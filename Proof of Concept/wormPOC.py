#!/usr/bin/env python3

from sys import argv
import os

script = argv
name = str(script[0])

cmd = 'start payload.txt'
os.system(cmd)
os.mkdir('clone')
os.system(r"cp payload.txt clone")
os.system(r"cp " + name + " clone")
