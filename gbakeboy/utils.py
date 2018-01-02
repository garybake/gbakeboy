

def hex2int(hex_string):
    return int(hex_string, 16)


def print_bin_16(val):
    """
    Print 16 bit int in binary
    """
    return "{0:b}".format(val).zfill(16)


def print_bin_8(val):
    """
    Print 8 bit int in binary
    """
    return "{0:b}".format(val).zfill(8)
