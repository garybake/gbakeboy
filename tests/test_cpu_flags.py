import unittest

from gbakeboy import Cpu
from gbakeboy import Memory
from gbakeboy import hex2int as h2i
from gbakeboy import print_bin_8


class test_cpu_flags(unittest.TestCase):

    def setUp(self):
        mem = Memory()
        self.cpu = Cpu(mem)
        self.cpu.set_register_16('AF', 0)

    def test_flags(self):
        cpu = self.cpu
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "00000000")

    def test_flags_Z(self):
        cpu = self.cpu
        cpu.set_flags(['Z'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "10000000")

    def test_flags_N(self):
        cpu = self.cpu
        cpu.set_flags(['N'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "01000000")

    def test_flags_H(self):
        cpu = self.cpu
        cpu.set_flags(['H'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "00100000")

    def test_flags_C(self):
        cpu = self.cpu
        cpu.set_flags(['C'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "00010000")

    def test_flags_multiple(self):
        cpu = self.cpu
        cpu.set_flags(['Z', 'H'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "10100000")

    def test_flags_all(self):
        cpu = self.cpu
        cpu.set_flags(['Z', 'N', 'H', 'C'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "11110000")

    def test_flags_none(self):
        cpu = self.cpu
        cpu.set_flags(['H'])
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "00100000")

        cpu.set_flags(False)
        flags = cpu.get_F()
        flags_string = print_bin_8(flags)
        self.assertEqual(flags_string, "00000000")

    @unittest.skip("TODO")
    def test_invalid_flag(self):
        pass
