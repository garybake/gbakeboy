import unittest

from gbakeboy import Memory


class test_memory(unittest.TestCase):

    def setUp(self):
        self.mem = Memory()

    def test_init(self):
        self.assertEqual(len(self.mem.memory), 65536)
        self.assertEqual(sum(self.mem.memory), 0)

    def test_load(self):
        pass

    def test_read(self):
        pass
