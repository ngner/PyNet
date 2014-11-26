#!/usr/bin/python3

''' Takes IP address as input and outputs table of biinary octets

 first_octet    second_octet     third_octet    fourth_octet'''


net_in = input("Please enter an IP address: ")
octets = net_in.split(".")
print("{:>20} {:>20} {:>20} {:>20}".format("first_octet", "second_octet", "third_octet", "fourth_octet"))
print("{:>20} {:>20} {:>20} {:>20}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))


      

