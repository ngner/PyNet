#!/usr/bin/env python

in_address = str(input(" /24 address please : "))

address = in_address.split(".")
address[3] = "0"

print address
