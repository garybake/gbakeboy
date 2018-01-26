
import logging
from .settings import MAX_CART_BYTES


class Cartridge:
    memory = bytearray(MAX_CART_BYTES)

    def __init__(self, rom_file):
        for i in range(0, MAX_CART_BYTES):
            self.memory[i] = 0

        with open(rom_file, mode='rb') as f:
            data = f.read()

        logging.info("loading cart data into loc 0x00 and up.")
        for addr in range(0, min(len(data), MAX_CART_BYTES)):
            self.memory[addr] = data[addr]

    # TODO - make generic memdevice object
    def read_byte(self, addr):
        # gets an 16bit int addr and returns the 8bit int content of memory
        if addr >= MAX_CART_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range')

        val = self.memory[addr]
        logging.debug('reading cart mem {0:X} is val {1:X}'.format(addr, val))
        return self.memory[addr]

        # self.memprint(0, MAX_CART_BYTES)

    # def memprint(self, offset, bytes, mode='hex'):
    #     if mode == 'hex':
    #         for i in range(0, bytes, 2):
    #             logging.info('{0:X}:\t {1:02X}\t{2:02X}'.format(i+offset, self.memory[i+offset], self.memory[i+1+offset]))
    #     elif mode == 'bin':
    #         for i in range(0, bytes):
    #             logging.info('{0:X}:\t {1:08b}'.format(i+offset, self.memory[i+offset]))