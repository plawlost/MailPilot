import unittest
from mailpilot.utils import validate_email, file_exists

class TestUtils(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_file_exists(self):
        self.assertTrue(file_exists(__file__))  # Current file should exist
        self.assertFalse(file_exists("nonexistent_file.xyz"))

if __name__ == '__main__':
    unittest.main()
