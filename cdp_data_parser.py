#!/usr/bin/python3


'''
create a dictionary of network devices:
network_devices = {
     'SW1': { 'ip': '10.1.1.22', 'model': 'WS-C2950-24', 'vendor': 'cisco', 'device_type': 'switch' },
     'R1': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
      ...
     'R5': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
 }
 '''

import cdp_data
import pprint

network_devices = {}

attributes = ["IP address: ", "Capabilities:", "Platform:"]
names = ["ip", "device_type", "vendor", "model"]

def get_hostname():
    hosts = []
    for attr in dir(cdp_data):
        if not attr.startswith('__') and not attr.endswith("detail"):
            text = vars(cdp_data)[attr]
            for line in text.split("\n"):
                if ">show cdp neigh" in line:
                    hosts.append(line[:line.find(">show cdp neigh")])
    return hosts


def get_attribute(host, attribute):
    if host == "SW1":
        text = cdp_data.r1_show_cdp_neighbors_detail
    else:
        text = cdp_data.sw1_show_cdp_neighbors_detail

    device_details = text.split("--------------------------")
    for detail in device_details:
        if "Device ID: " + host in detail:
            detail = detail.partition(attribute)[2].partition(",")[0]
            detail = detail.split("\n")[0]
            return [detail.strip()]

def get_neighbours(host):
    for attr in dir(cdp_data):
        if not attr.startswith('__') and not attr.endswith("detail"):
            text = vars(cdp_data)[attr]
            neighbours = []
            if host + ">show cdp neighbors" in text:
                start = False
                for line in text.split("\n"):
                    if "Device ID" in line:
                        start = True
                    if len(line) < 3:
                        start = False
                    if not "Device ID" in line and start == True:
                        neighbours.append(line.split()[0])
                return neighbours
                        
                        
    return hosts
          
    


hosts = get_hostname()

for host in hosts:
    hosts_attributes = []
    for attr in attributes:
        attribute = get_attribute(host, attr)
        if attr == "Capabilities:":
            attribute = [attribute[0].split(" ")[0]]
        if attr == "Platform:":
            attribute = attribute[0].split(" ")
        hosts_attributes.extend(attribute)
    hosts_attributes = dict(zip(names, hosts_attributes))
    network_devices[host] = hosts_attributes

pprint.pprint(network_devices)

for key in network_devices:
    network_devices[key]['adjacent_devices'] = get_neighbours(key)



pprint.pprint(network_devices)
        



    
    





        
