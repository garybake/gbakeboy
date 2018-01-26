
import logging
from .ram_device import RamDevice
from .settings import MAX_CART_BYTES

class Cartridge(RamDevice):

    def __init__(self, rom_file):
        super().__init__(0, 0x7fff)
        self.name = 'Cartridge'
        self.load_from_file(rom_file)
