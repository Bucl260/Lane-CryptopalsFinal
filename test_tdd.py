import unittest
from tdd import hex_to_base64

class TestHexToBase64(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(hex_to_base64(""), "")

if __name__ == '__main__':
    unittest.main()
