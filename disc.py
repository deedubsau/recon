#!/usr/bin/python

import subprocess
import netifaces as ni

#print ni.ifaddresses('eth0')
v_addr = ni.ifaddresses('eth0')[2][0]['addr']
v_mask = ni.ifaddresses('eth0')[2][0]['netmask']

# depending upon ipcalcs implementation of cidr tables. saves having to implement and troubleshoot myself
#from subprocess import call
v_ipcalc = subprocess.Popen(["ipcalc", v_addr + "/" + v_mask], stdout=subprocess.PIPE)

for line in iter(v_ipcalc.stdout.readline,''):
	if "Hosts" in line:
		v_hosts = line.rstrip()
		break



for line in iter(v_ipcalc.stdout.readline,''):
        if "Hosts" in line:
                v_hosts = line.rstrip()
                break

print "Total Hosts on subnet: " + v_hosts.rsplit(':',1)[1].rsplit(' ')[1]
# likely gw's





