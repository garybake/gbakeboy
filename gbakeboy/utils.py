import logging


class Color(object):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def log_h1(str):
    logging.info('\n' + Color.YELLOW +
                 Color.UNDERLINE + str + Color.END + '\n')


def log_h2(str):
    logging.info('\n\n' + Color.GREEN + str + Color.END)


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


def get_bit_value(val, place):
    """
    Return the truthness of the bit in place place
    from 8 or 16 bit val
    """
    place_val = 2**place
    return val & place_val != 0


def twos_comp_8(val):
    bits = 9
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val

def hex_array(arr):
    # return [hex(i) for i in arr]
    # TODO: fix this
    ret = []
    for a in arr:
        if type(a) is str:
            ret.append(a)
        else:
            ret.append(hex(a))
    return ret