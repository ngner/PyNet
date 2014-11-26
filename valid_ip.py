def valid_ip(ip_addr):
    "Returns True or False for string input if it is a valid IP address"""
    
    valid_ip = True
    
    # Make sure IP has four octets
    octets = ip_addr.split('.')
    if len(octets) != 4:
        print("\nOoops, you don't have 4 octets - try again.")
        valid_ip = False
    
    # convert octet from string to int
    for i,octet in enumerate(octets):
    
        try:
            octets[i] = int(octet)
        except ValueError:
            # couldn't convert octet to an integer
            valid_ip = False

    # Go to next iteration of while loop if I don't have 4 integers
    if not valid_ip:    
        print("\nYou entered an octet that wasn't an integer (or a blank \n octet) - that's not going to work.")

    # map variables to elements of octets list
    first_octet, second_octet, third_octet, fourth_octet = octets
    
    # Check first_octet meets conditions
    if first_octet < 1:
        valid_ip = False
        print("First Octet less than 1")
    elif first_octet > 223:
        valid_ip = False
        print("First Octet greater than 223 (multicast)")
    elif first_octet == 127:
        valid_ip = False
        print("First Octet is 127 so a loopback")
    
    # Check 169.254.X.X condition
    if first_octet == 169 and second_octet == 254:
        valid_ip = False
        print(" This is 169.254. so not valid")
    
    # Check 2nd - 4th octets
    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            valid_ip = False
            print("2nd to 4th octet not in range 0 and 255")

    return valid_ip

   
