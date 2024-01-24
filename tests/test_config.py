import unittest
from unittest.mock import patch
from mailpilot.config import MailPilotConfig

class TestMailPilotConfig(unittest.TestCase):

    def setUp(self):
        self.config = MailPilotConfig()

    @patch('configparser.ConfigParser.write')
    def test_save_config(self, mock_write):
        self.config.save_config()
        mock_write.assert_called()

    @patch('configparser.ConfigParser.read')
    def test_load_config(self, mock_read):
        self.config.load_config()
        mock_read.assert_called()

    def test_set_and_get_smtp_settings(self):
        test_smtp_settings = {
            'host': 'smtp.test.com',
            'port': 587,
            'user': 'user@test.com',
            'password': 'password123'
        }
        self.config.set_smtp_settings(**test_smtp_settings)

        retrieved_settings = self.config.get_smtp_settings()
        self.assertEqual(retrieved_settings, test_smtp_settings)

    # Additional tests can be added here to cover more functionalities

if __name__ == '__main__':
    unittest.main()
