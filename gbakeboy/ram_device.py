
import logging
from .settings import MAX_CART_BYTES

class RamDevice:
    start_address = 0
    end_address = 0
    size = 0
    memory = None  # bytearray
    name = 'Ram'

    def __init__(self, start, end):
        self.start_address = start
        self.end_address = end
        self.size = end - start
        self.memory = bytearray(self.size)

        for i in range(0, self.size):
            self.memory[i] = 0

    def read_byte(self, addr, verbose=True):
        # gets an 16bit int addr and returns the 8bit int content of memory
        if addr < self.start_address or addr >= self.end_address:
            raise MemoryError('Attempt to read outside of Memory range: {}'.format(addr))

        local_addr = addr - self.start_address
        val = self.memory[local_addr]
        if verbose:
            logging.debug('reading {0} mem {1:X} is val {2:X}'.format(self.name, addr, val))
        return self.memory[local_addr]

    def write_byte(self, addr, val):
        if addr < self.start_address or addr >= self.end_address:
            raise MemoryError('Attempt to read outside of Memory range: {}'.format(addr))

        local_addr = addr - self.start_address
        logging.debug('setting {0} mem {1:X} to val {2:X}'.format(self.name, addr, val))
        self.memory[local_addr] = val

    def load_from_file(self, rom_file):
        with open(rom_file, mode='rb') as f:
            data = f.read()

        logging.info("loading cart data into loc 0x00 and up.")
        for addr in range(self.start_address, min(len(data) + self.start_address, self.end_address)):
            self.memory[addr] = data[addr]

    def mem_print(self, offset=None, bytes=None, mode='hex'):
        if not offset:
            offset = self.start_address
        if not bytes:
            bytes = self.size - 1
        if mode == 'hex':
            for i in range(0, bytes, 2):
                logging.info('{0:X}:\t {1:02X}\t{2:02X}'.format(i+offset, self.memory[i], self.memory[i+1]))
        elif mode == 'bin':
            for i in range(0, bytes):
                logging.info('{0:X}:\t {1:08b}'.format(i+offset, self.memory[i], self.memory[i+1]))