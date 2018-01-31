import logging
from .utils import hex2int as h2i
from .settings import MAX_MEMORY_BYTES
from .sound import Sound


class Memory:
    memory = bytearray(MAX_MEMORY_BYTES)
    cartridge = None
    sound = Sound()

    def __init__(self):
        for i in range(0, len(self.memory)):
            self.memory[i] = 0

    def load(self, data, offset, start=0, end=0xFFFF):
        logging.info("loading data into loc %X and up." % offset)
        for i in range(max(0, start), min(len(data), end)):
            addr = int(i+offset)
            if addr >= MAX_MEMORY_BYTES:
                raise MemoryError
            self.memory[addr] = data[i]

    def write_byte(self, addr, val, verbose=True):
        if addr >= MAX_MEMORY_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range: {}'.format(addr))

        if self.cartridge and addr > 0xFF and addr < 0x4000:
            # Cartridge ROM
            # TODO remove bios rom mask
            return self.cartridge.write_byte(addr, verbose)
        elif self.cartridge and addr > 0xFF10 and addr < 0xFF3F:
            return self.sound.write_byte(addr, verbose)

        if verbose:
            logging.debug('setting mem {0:X} to val {1:X}'.format(addr, val))
        self.memory[addr] = val

    def write_word(self, addr, val, verbose=True):
        # TODO not sure of the order
        byte_lo = (val >> 8)
        byte_hi = (val & 0xFF)
        self.write_byte(addr, byte_hi, verbose)
        self.write_byte(addr + 1, byte_lo, verbose)

    def read_byte(self, addr, verbose=True):
        # gets an 16bit int addr and returns the 8bit int content of memory
        if addr >= MAX_MEMORY_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range')

        if self.cartridge and addr > 0xFF and addr < 0x4000:
            # Cartridge ROM
            # TODO remove bios rom mask
            return self.cartridge.read_byte(addr, verbose)
        elif self.cartridge and addr > 0xFF10 and addr < 0xFF3F:
            return self.sound.read_byte(addr, verbose)

        val = self.memory[addr]
        if verbose:
            logging.debug('reading unallocated mem {0:X} is val {1:X}'.format(addr, val))
        return self.memory[addr]

    def read_word(self, addr, verbose=True):
        # TODO
        # gets an 16bit int addr and returns the 16 bit int content of memory
        if addr >= MAX_MEMORY_BYTES or addr < 0:
            raise MemoryError('Attempt to read outside of Memory range')
        return ((self.memory[addr+1] << 8) | self.memory[addr])

    def mem_print(self, offset, bytes, mode='hex'):
        if mode == 'hex':
            for i in range(0, bytes, 2):
                logging.info('{0:X}:\t {1:02X}\t{2:02X}'.format(i+offset, self.read_byte(i+offset, False), self.read_byte(i+1+offset, False)))
        elif mode == 'bin':
            for i in range(0, bytes):
                logging.info('{0:X}:\t {1:08b}'.format(i+offset, self.memory[i+offset]))

    def memprintat(self, offset, mode='hex'):
        if mode == 'hex':
            logging.info('{0:X}:\t {1:x}'.format(offset, self.memory[offset]))
        elif mode == 'bin':
            logging.info('{0:X}:\t {2:08b}'.format(offset, self.memory[offset]))

    def load_cartridge(self, cartridge):
        self.cartridge = cartridge
