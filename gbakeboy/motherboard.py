
import logging

from .cpu import Cpu
from .memory import Memory
from .utils import hex2int as h2i
from .settings import BIOS_FILE


class Motherboard:
    """
    Essentially the motherboard
    """

    def __init__(self):
        self.mem = Memory()
        self.cpu = Cpu(self.mem)
        self.load_bios()

    def load_bios(self):
        logging.info('loading bios rom')
        with open(BIOS_FILE, mode='rb') as f:
            boot = f.read()

        self.mem.load(boot, h2i('0000'))

    def tick(self):
        cycles = self.cpu.execute()
        return cycles

    def load_cartridge(self, cartridge):
        logging.info('loading cartridge')
        self.mem.load(cartridge.rom_data, 0xFF + 1, end=0x014F)
