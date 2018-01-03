#!/usr/bin/env python3

import logging
import sys

from gbakeboy import Motherboard


def loop(gb):
    cycles = 0
    gb.cpu.print_registers()
    for i in range(1, 5):
        logging.debug('--------tick {}'.format(i))
        cycles += gb.tick()
        gb.cpu.print_registers()
        # cycles += gb.tick()
        # gb.cpu.print_registers()

    logging.debug('{} cycles executed.'.format(cycles))


def main(argv):
    logging.debug('initialising...')
    gb = Motherboard()
    logging.debug('init done')

    logging.debug('loading rom')
    if len(argv) > 1 and argv[1]:
        logging.debug('argument supplied: {}'.format(argv[1]))
        # with open(argv[1], mode='rb') as f:
        #     # f.read() returns an array of bytes
        #     # rom = f.read()
        #     rom = Rom(f.read())
        #     # logging.debug(rom)
    else:
        logging.error('no argument supplied, supply a file')

    loop(gb)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv)
