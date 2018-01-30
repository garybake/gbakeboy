
import logging
from .ram_device import RamDevice
from .settings import LICENCEE_MAP, MBC_MAP, ROM_SIZE_MAP, RAM_SIZE_MAP


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
        self.licensee_code = self.get_licencee()
        self.sgb_support = self.get_sgb_support()
        self.mbc_type = self.get_mbc_type()
        self.rom_size = self.get_rom_size()
        self.ram_size = self.get_ram_size()

    def log_header(self):
        logging.info("Cart title: {}".format(self.title))
        logging.info("Cart manufacturer: {}".format(self.manufacturer_code))
        logging.info("Cart CBG only: {}".format(self.cbg_only))
        logging.info("Cart licensee: {}".format(self.licensee_code))
        logging.info("Cart SGB support: {}".format(self.sgb_support))
        logging.info("Cart MBC type: {}".format(self.mbc_type))
        logging.info("Cart ROM size: {}".format(self.rom_size))
        logging.info("Cart RAM size: {}".format(self.ram_size))

    def get_cgb_only(self):
        # 0143 - CGB Flag
        # 80h - Game supports CGB functions, but works on old gameboys also.
        # C0h - Game works on CGB only (physically the same as 80h).
        # TODO I can't find an example of this
        # flag = self.read_byte(0x0143)
        return False

    def get_licencee(self):
        code = self.read_text(0x0144, 0x0145)
        return LICENCEE_MAP.get(code, 'Unknown')

    def get_sgb_support(self):
        # 0146 - SGB Flag
        # 00h = No SGB functions (Normal Gameboy or CGB only game)
        # 03h = Game supports SGB functions
        support = False
        if self.read_byte(0x0146) == 0x03:
            support = True
        return support

    def get_mbc_type(self):
        code = self.read_byte(0x0147)
        return MBC_MAP.get(code, 'Unknown')

    def get_rom_size(self):
        code = self.read_byte(0x0148)
        return ROM_SIZE_MAP.get(code, 'Unknown')

    def get_ram_size(self):
        code = self.read_byte(0x0149)
        return RAM_SIZE_MAP.get(code, 'Unknown')
