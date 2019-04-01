import unittest
key_schedule = __import__("key_schedule.py")
keyExpand = key_schedule.keyExpand

class TestStringMethods(unittest.TestCase):

    def test_keyExpand(self):
        k = '2b7e151628aed2a6abf7158809cf4f3c'
        key = bytearray()

        w0 = bytearray('2b7e1516', 'UTF-8')
        w1 = bytearray('2b7e1516', 'UTF-8')
        w2 = bytearray('2b7e1516', 'UTF-8')
        w3 = bytearray('2b7e1516', 'UTF-8')

        key.extend(map(ord, k))
        wordArray = [w0, w1, w2, w3]
        self.assertEqual(keyExpand(key, wordArray, 4, 4, 10), 'FOO')

if __name__ == '__main__':
    unittest.main()