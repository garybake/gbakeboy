import unittest

from gbakeboy import Cpu
from gbakeboy import Memory
from gbakeboy import hex2int as h2i


class test_memory(unittest.TestCase):

    def setUp(self):
        mem = Memory()
        self.cpu = Cpu(mem)

    def test_init(self):
        cpu = self.cpu
        mem = self.cpu.mem

        self.assertNotEqual(mem, None)

        self.assertEqual(cpu._A, h2i("B0"))
        self.assertEqual(cpu._F, h2i("01"))
        self.assertEqual(cpu._PC, 0)
