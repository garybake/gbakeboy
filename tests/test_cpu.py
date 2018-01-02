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

        self.assertEqual(cpu.A, h2i("B0"))
        self.assertEqual(cpu.F, h2i("01"))
        self.assertEqual(cpu.PC, 0)

    # def test_flags(self):
    #     cpu = self.cpu
    #     flags = cpu.get_F()
    #     flags_string = '{0:b}'.format(flags)
    #     # print('Flags: {}'.format(flags))
    #     self.assertEqual(flags_string, "gary")
