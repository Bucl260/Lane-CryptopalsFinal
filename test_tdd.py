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
        
    def test_conversion(self):
        hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        expected_base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(hex_to_base64(hex_string), expected_base64)

if __name__ == '__main__':
    unittest.main()
