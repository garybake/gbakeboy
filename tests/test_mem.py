import unittest

from gbakeboy import Memory
from gbakeboy import hex2int as h2i
from gbakeboy import MAX_MEMORY_BYTES

mem_start = h2i('0000')


class test_memory(unittest.TestCase):

    def setUp(self):
        self.mem = Memory()

    def load_data(self, mem):
        # Load some test data into memory
        data = bytes([0x13, 0x01, 0x00, 0x01, 0x08, 0x09])
        self.mem.load(data, mem_start)

    def test_init(self):
        self.assertEqual(len(self.mem.memory), MAX_MEMORY_BYTES)
        self.assertEqual(sum(self.mem.memory), 0)

    def test_load(self):
        # Load some data
        data = bytes([0x13, 0x01, 0x00, 0x00, 0x08, 0x09])
        self.mem.load(data, mem_start)

        read_data = self.mem.read_byte(mem_start)
        self.assertEqual(read_data, 0x13)
        read_data = self.mem.read_byte(mem_start + 1)
        self.assertEqual(read_data, 0x01)
        read_data = self.mem.read_byte(mem_start + 4)
        self.assertEqual(read_data, 0x08)

        # Test we can overwrite data
        data = bytes([0x14, 0x02, 0x01, 0x08, 0xA8, 0x09])
        self.mem.load(data, mem_start)

        read_data = self.mem.read_byte(mem_start + 1)
        self.assertEqual(read_data, 0x02)
        read_data = self.mem.read_byte(mem_start + 4)
        self.assertEqual(read_data, 0xA8)

    def test_read_byte(self):
        self.load_data(self.mem)

        read_data = self.mem.read_byte(mem_start)
        self.assertEqual(read_data, 0x13)

        read_data = self.mem.read_byte(mem_start + 2)
        self.assertEqual(read_data, 0x00)

    def test_read_byte_outside_mem_range(self):
        self.load_data(self.mem)
        read_data = self.mem.read_byte(MAX_MEMORY_BYTES - 1)
        self.assertEqual(read_data, 0x00)

        with self.assertRaises(MemoryError):
            self.mem.read_byte(MAX_MEMORY_BYTES)

        with self.assertRaises(MemoryError):
            self.mem.read_byte(0x00 - 2)

    def test_read_word(self):
        self.load_data(self.mem)

        read_data = self.mem.read_word(mem_start)
        self.assertEqual(read_data, 0x0113)

        read_data = self.mem.read_word(mem_start + 4)
        self.assertEqual(read_data, 0x0908)

    def test_read_word_outside_mem_range(self):
        self.load_data(self.mem)

        with self.assertRaises(MemoryError):
            self.mem.read_word(MAX_MEMORY_BYTES)

        with self.assertRaises(MemoryError):
            self.mem.read_word(0x00 - 2)
