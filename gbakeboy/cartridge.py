
import logging


class Cartridge:
    rom_data = bytearray()

    def __init__(self, rom_file):
        with open(rom_file, mode='rb') as f:
            self.rom_data = f.read()
        # self.mem.load(self.rom_data, 0xFF + 1)
