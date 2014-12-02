#!/bin/env python3


''' Opens CDP file "file_path" and finds the remote hostname, remote IP, remote model
 and remote vendor'''


import re
import pprint

def make_cdp_str(file):
    with open(file, mode='r') as cdp:
        return cdp.read()

def find_details(cdp_str):
    hostnames = re.findall(r'Device ID:\s*(\w*)', cdp_str)
    ips = re.findall(r'IP address:\s*([\d.]+)', cdp_str)
    platforms = re.findall(r'Platform:\s(\w+\s\w+)', cdp_str)
    return {"remote_hosts": hostnames, "IPs": ips, "platform": platforms}




if __name__ == "__main__":
    cdp_str = make_cdp_str(r'./CDP_DATA/sw1_cdp.txt')
    details = find_details(cdp_str)
    pprint.pprint(details)
    
    
