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

# summarising available hosts
print "Total Hosts on subnet: " + v_hosts.rsplit(':',1)[1].rsplit(' ')[1]
# likely gw's, check first three and last three IP addresses in block

## check if first three and last three are valid IP addresses. only rely on arp response.

## if valid, attempt to route traffic manually via them (ttl = 0, get ICMP ttl expired in transit?)


# identify common vsrp/hsrp mac addresses (cisco hsrp groups, etc)


# identify live hosts on local layer 2


# identify duplicate hosts (same mac)


# identify duplicate hosts (iterative mac)


