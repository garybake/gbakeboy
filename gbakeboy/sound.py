import logging
from .ram_device import RamDevice

class Sound(RamDevice):

    def __init__(self):
        super().__init__(0xFF10, 0xFF3F)
        self.name = 'Sound'
