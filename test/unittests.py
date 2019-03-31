import unittest
key_schedule = __import__("key_schedule.py")
keyExpand = key_schedule.keyExpand

class TestStringMethods(unittest.TestCase):

    def test_keyExpand(self):
        key = "8F0A5EB7BE9F67B883CEF7003626340E" #MD5 of Hello Test
        word = (0x00, 0x01, 0x02, 0x03) #Dummy Word
        self.assertEqual(keyExpand(key, word, 4, 4, 10), 'FOO')

if __name__ == '__main__':
    unittest.main()