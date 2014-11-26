#!/usr/bin/python3

''' Take a BGP table output of the form below and return a table of prefix and AS Path'''


output = '''*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i
*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i
*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i
*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i'''




def text_parse(text):
    bgp_table = {}
    for line in text.split('\n'):
        entries = line.split()
        ip_prefix = entries[1]
        as_path = entries[4:-1]
        bgp_table[ip_prefix] = as_path
    return bgp_table

bgp_table = text_parse(output)
print('{:<20} {:<30}'.format('ip_prefix', 'as_path'))
for key in bgp_table:
    prefix = key
    path = bgp_table[prefix]
    print('{:<20} {:<30}'.format(prefix, str(path)))

        
