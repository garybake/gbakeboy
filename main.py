#!/usr/bin/env python3

import logging
import sys

from gbakeboy import Motherboard, utils, Cartridge

START_WATCHING = 24590
MAX_TICKS = 24645


def loop(gb):
    cycles = 0
    for tick_count in range(1, MAX_TICKS):
        cycles += gb.tick()
        if tick_count > START_WATCHING:
            utils.log_h2('Tick {}'.format(tick_count-1))
            logging.getLogger().setLevel(logging.DEBUG)
            gb.cpu.print_registers()

    logging.debug('{} cycles executed.'.format(cycles))

    # gb.cpu.mem.mem_print(0xF1, 0x1A)
    # gb.cpu.mem.sound.mem_print()


def main(argv):
    logging.debug('initialising...')
    gb = Motherboard()
    logging.debug('init done')

    logging.debug('loading rom')
    if len(argv) > 1 and argv[1]:
        logging.debug('argument supplied: {}'.format(argv[1]))
        cartridge = Cartridge(argv[1])
        gb.load_cartridge(cartridge)
    else:
        logging.error('no argument supplied, supply a file')

    loop(gb)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    utils.log_h1('START')
    main(sys.argv)
