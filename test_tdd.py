import unittest
from tdd import hex_to_base64

class TestHexToBase64(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(hex_to_base64(""), "")
        
    def test_three_bytes(self):
        self.assertEqual(hex_to_base64("4d616e"), "TWFu")
    
    def test_single_byte(self):
        self.assertEqual(hex_to_base64("4d"), "TQ==")

    def test_two_bytes(self):
        self.assertEqual(hex_to_base64("4d61"), "TWE=")

if __name__ == '__main__':
    unittest.main()
