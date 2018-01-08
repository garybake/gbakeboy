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
