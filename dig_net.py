#!/bin/env python3

''' runs a "dig" on all IPs in the range and displays'''


from subprocess import Popen, PIPE
for i in range(1, 254):
	cmd = "dig -x 172.120.16." + str(i)
	print cmd
	print Popen(cmd, shell=True, stdout=PIPE).stdout.read()
	
