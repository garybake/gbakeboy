
import logging

from .cpu import Cpu
from .memory import Memory
from .utils import hex2int as h2i
from .settings import bios_file


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
        with open(bios_file, mode='rb') as f:
            boot = f.read()

        self.mem.load(boot, h2i('0000'))

    def load_rom(self, rom, location):
        pass

    def tick(self):
        self.cpu.execute()
