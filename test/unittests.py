import unittest
from src.key_schedule import keyExpand

class TestStringMethods(unittest.TestCase):

    def test_keyExpand_1(self):
        key = 0x2b7e151628aed2a6abf7158809cf4f3c
        self.assertEqual(keyExpand(key, 4, 4, 10), [0x2b7e1516, 0x28aed2a6, 0xabf71588, 0x09cf4f3c])



if __name__ == '__main__':
    unittest.main()