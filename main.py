#!/usr/bin/env python3

import logging
import sys

from gbakeboy import Motherboard, utils

START_WATCHING = 24578
MAX_TICKS = 24596


def loop(gb):
    cycles = 0
    for tick_count in range(1, MAX_TICKS):
        cycles += gb.tick()
        if tick_count > START_WATCHING:
            utils.log_h2('Tick {}'.format(tick_count-1))
            logging.getLogger().setLevel(logging.DEBUG)
            gb.cpu.print_registers()

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
    logging.basicConfig(level=logging.INFO)
    utils.log_h1('START')
    main(sys.argv)
