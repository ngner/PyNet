#!/bin/env python3

import os
import re
import pprint


def find_item(pattern, ospf_data):
    text = re.search(pattern, ospf_data)
    if text:
        text = text.group(1)
        return text
    else:
        #print(pattern, ' not found')
        return ''

def ospf_data(file_name):
    with open(file_name) as ospf:
        interface_list = re.split(r'\n\b', ospf.read())
        return interface_list

pattern_dict = {'Int': r'^(.*) is up, line protocol is up',
                'IP': r'\s*Internet Address\s([\d./]+)',
                'Area':  r'\s*Area (\d+)',
                'Type': r'\s*Network Type (\w+)',
                'Cost': r'\s*Cost: (\d+)',
                'Hello': r'\s* Hello (\d+)',
                'Dead': r'\s*Dead (\d+)'}

if __name__ == "__main__":
    
    file_name = 'ospf_data.txt'
    
    os.chdir(r'class7/OSPF_DATA')
    
    
    ospf_interfaces = ospf_data(file_name)
    ospf_interfaces.pop(0)

    

    for interface in ospf_interfaces:
        ospf_info = {}
        for key in pattern_dict.keys():
            ospf_info[key] = find_item(pattern_dict[key], interface)
        for key, value in ospf_info.items():
            print(' {:<7}{}'.format(key + ':', value))

