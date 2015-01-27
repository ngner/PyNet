
def NetMask(mask_length):
    bits = ""
    for i in range(mask_length):
        bits = bits + "1"

    for i in range(32 - mask_length):
        bits = bits + "0"

    octets = []

    for octet in range(4):
        octets.append(str(int(bits[(octet * 8):((octet + 1) * 8)], base=2)))
    return ".".join(octets)
    
    
if __name__ == "__main__":
    import sys
    mask_length = int(sys.argv[1])
    print NetMask(mask_length)
