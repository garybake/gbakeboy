import unittest

from gbakeboy import Motherboard
from gbakeboy import utils


class test_motherboard(unittest.TestCase):

    def setUp(self):
        self.motherboard = Motherboard()

    def test_init(self):
        mb = self.motherboard

        self.assertNotEqual(mb.mem, None)
        self.assertNotEqual(mb.cpu, None)

        mem_0 = mb.mem.read_byte(0)
        self.assertEqual(mem_0, utils.hex2int("31"))

        mem_end = mb.mem.read_byte(0xff)
        self.assertEqual(mem_end, utils.hex2int("50"))

        # self.assertEqual(cpu.A, h2i("01"))

    def test_bios_loaded(self):
        """
        Check we have loaded the bios by checking the first and last bits
        are correct in ram
        TODO: Do a full check of all bios bytes using CRC or something?
        """

        mb = self.motherboard

        mem_0 = mb.mem.read_byte(0)
        self.assertEqual(mem_0, utils.hex2int("31"))

        mem_end = mb.mem.read_byte(0xff)
        self.assertEqual(mem_end, utils.hex2int("50"))

    def test_bios_tick(self):
        mb = self.motherboard
        cycles = 0

        cycles += mb.tick()
        self.assertEqual(cycles, 12)

        cycles += mb.tick()
        self.assertEqual(cycles, 16)

        cycles += mb.tick()
        self.assertEqual(cycles, 28)
