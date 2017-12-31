
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
        logging.debug('loading bios rom')
        with open(BIOS_FILE, mode='rb') as f:
            boot = f.read()

        self.mem.load(boot, h2i('0000'))

    def load_rom(self, rom, location):
        pass

    def tick(self):
        cycles = self.cpu.execute()
        return cycles
