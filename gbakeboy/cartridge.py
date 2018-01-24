
import logging


class Cartridge:
    rom_data = bytearray()

    def __init__(self, rom_file):
        with open(rom_file, mode='rb') as f:
            data = f.read()
        self.rom_data = data[0x100:]
