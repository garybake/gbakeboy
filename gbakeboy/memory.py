import logging
from .utils import hex2int as h2i
from .settings import MAX_MEMORY_BYTES


class Memory:
    memory = bytearray(MAX_MEMORY_BYTES)

    def __init__(self):
        for i in range(0, len(self.memory)):
            self.memory[i] = 0

    def load(self, data, offset, start=0, end=0xFFFF):
        logging.debug("loading data into loc %X and up." % offset)
        for i in range(max(0, start), min(len(data), end)):
            addr = int(i+offset)
            if addr >= MAX_MEMORY_BYTES:
                raise MemoryError
            self.memory[addr] = data[i]

    def write_byte(self, addr, val):
        if addr >= MAX_MEMORY_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range: {}'.format(addr))
        logging.debug('setting mem {0:X} to val {1:X}'.format(addr, val))
        self.memory[addr] = val

    def write_word(self, addr, val):
        # TODO
        pass

    def read_byte(self, addr):
        # gets an 16bit int addr and returns the 8bit int content of memory
        if addr >= MAX_MEMORY_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range')
        return self.memory[addr]

    def read_word(self, addr):
        # gets an 16bit int addr and returns the 16 bit int content of memory
        if addr >= MAX_MEMORY_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range')
        return ((self.memory[addr+1] << 8) | self.memory[addr])

    def memprint(self, offset, bytes, mode='hex'):
        if mode == 'hex':
            for i in range(0, bytes, 2):
                logging.info('{0:X}:\t {1:02X}\t{2:02X}'.format(i+offset, self.memory[i+offset], self.memory[i+1+offset]))
        elif mode == 'bin':
            for i in range(0, bytes):
                logging.info('{0:X}:\t {1:08b}'.format(i+offset, self.memory[i+offset]))

    def memprintat(self, offset, mode='hex'):
        if mode == 'hex':
            logging.info('{0:X}:\t {1:x}'.format(offset, self.memory[offset]))
        elif mode == 'bin':
            logging.info('{0:X}:\t {2:08b}'.format(offset, self.memory[offset]))
