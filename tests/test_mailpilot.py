import unittest
from unittest.mock import patch
from mailpilot import MailPilotApplication, MailPilotConfig

class TestMailPilot(unittest.TestCase):

    def setUp(self):
        self.app = MailPilotApplication()
        self.app.config = MailPilotConfig()

    @patch('mailpilot.MailPilot.send_emails')
    def test_send_mail(self, mock_send_emails):
        subject = "Test Email"
        recipients = [{"name": "John Doe", "email": "johndoe@example.com"}]
        template = "<p>Hello, World!</p>"

        self.app.send_mail(subject, recipients, template)
        mock_send_emails.assert_called_once()

    # Additional tests can be added here to cover more functionalities

if __name__ == '__main__':
    unittest.main()
