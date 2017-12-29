import logging
from .utils import hex2int as h2i


class Memory:
    memory = bytearray(65536)

    def __init__(self):
        for i in range(0, len(self.memory)):
            self.memory[i] = 0

    def load(self, data, offset, start=0, end=0xFFFF):
        logging.debug("loading data into loc %X and up." % offset)
        for i in range(max(0, start), min(len(data), end)):
            self.memory[int(i+offset)] = data[i]

    def read_byte(self, addr):
        # gets an 16bit int addr and returns the 8bit int content of memory
        return self.memory[addr]

    def read_word(self, addr):
        # gets an 16bit int addr and returns the 16 bit int content of memory
        return ((self.memory[addr+1] << 8) | self.memory[addr])

    def memprint(self, offset, bytes, mode='hex'):
        if mode == 'hex':
            for i in range(0, bytes, 2):
                print('{0:X}:\t {1:02X}\t{2:02X}'.format(i+offset, self.memory[i+offset], self.memory[i+1+offset]))
        elif mode == 'bin':
            for i in range(0, bytes):
                print('{0:X}:\t {1:08b}'.format(i+offset, self.memory[i+offset]))

    def memprintat(self, offset, mode='hex'):
        if mode == 'hex':
            print('{0:X}:\t {1:x}'.format(offset, self.memory[offset]))
        elif mode == 'bin':
            print('{0:X}:\t {2:08b}'.format(offset, self.memory[offset]))
