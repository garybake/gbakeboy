import unittest

from gbakeboy import Cpu
from gbakeboy import Memory
from gbakeboy import hex2int as h2i


class test_cpu(unittest.TestCase):

    def setUp(self):
        mem = Memory()
        self.cpu = Cpu(mem)

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

    # def test_flags(self):
    #     cpu = self.cpu
    #     flags = cpu.get_F()
    #     flags_string = '{0:b}'.format(flags)
    #     # print('Flags: {}'.format(flags))
    #     self.assertEqual(flags_string, "gary")
