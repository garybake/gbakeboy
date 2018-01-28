
import logging
from .ram_device import RamDevice
from .settings import MAX_CART_BYTES

class Cartridge(RamDevice):

    def __init__(self, rom_file):
        super().__init__(0, 0x7fff)
        self.name = 'Cartridge'
        self.load_from_file(rom_file)
        self.parse_header()
        self.log_header()

    def parse_header(self):
        self.title = self.read_text(0x0134, 0x0143)
        # Manufacturer is only relavent on new carts
        self.manufacturer_code = self.read_text(0x013F, 0x0142)
        self.cbg_only = self.get_cgb_only()

        self.licensee_code = self.read_text(0x0144, 0x0145)



    def log_header(self):
        logging.info("Cart title: {}".format(self.title))
        logging.info("Cart manufacturer: {}".format(self.manufacturer_code))
        logging.info("Cart cbg only: {}".format(self.cbg_only))
        logging.info("Cart licensee: {}".format(self.licensee_code))



    def get_cgb_only(self):
        # 0143 - CGB Flag
        # 80h - Game supports CGB functions, but works on old gameboys also.
        # C0h - Game works on CGB only (physically the same as 80h).
        # TODO I can't find an example of this
        flag = self.read_word(0x0143)
        return True

