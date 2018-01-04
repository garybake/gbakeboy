import unittest

from gbakeboy import Cpu
from gbakeboy import Memory
from gbakeboy import hex2int as h2i
from gbakeboy import print_bin_8


class test_cpu(unittest.TestCase):

    def setUp(self):
        mem = Memory()
        self.cpu = Cpu(mem)

    def clear_registers(self):
        cpu = self.cpu
        cpu.set_register_16('AF', 0)
        cpu.set_register_16('BC', 0)
        cpu.set_register_16('DE', 0)
        cpu.set_register_16('HL', 0)
        cpu.set_register_16('SP', 0)
        cpu.set_register_16('PC', 0)

    def test_init(self):
        cpu = self.cpu
        mem = self.cpu.mem

        self.assertNotEqual(mem, None)

        self.assertEqual(cpu.A, h2i("01"))
        self.assertEqual(cpu.F, h2i("B0"))

        self.assertEqual(cpu.B, h2i("00"))
        self.assertEqual(cpu.C, h2i("13"))

        self.assertEqual(cpu.D, h2i("00"))
        self.assertEqual(cpu.E, h2i("D8"))

        self.assertEqual(cpu.H, h2i("01"))
        self.assertEqual(cpu.L, h2i("4D"))

        self.assertEqual(cpu.SP, h2i("FFFE"))
        self.assertEqual(cpu.PC, h2i("0"))
