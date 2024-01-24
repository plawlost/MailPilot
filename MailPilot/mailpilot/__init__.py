# Copyright [2024] [Yağız Erkam '@plawlost' Çelebi]

from .mailpilot import MailPilot
from .config import MailPilotConfig
from .utils import (
    validate_email, extract_name_email, file_exists, create_if_not_exists,
    validate_file_path, prompt_for_input, secure_input, read_json_file, write_json_file
)

__all__ = [
    'MailPilot', 'MailPilotConfig', 'validate_email', 'extract_name_email',
    'file_exists', 'create_if_not_exists', 'validate_file_path', 'prompt_for_input',
    'secure_input', 'read_json_file', 'write_json_file'
]

__version__ = '1.0.0'
__author__ = "Yağız Erkam '@plawlost' Çelebi"
__license__ = 'Apache License 2.0'

class MailPilotApplication:
    """
    Main Application Class for MailPilot
    This class provides a high-level interface for MailPilot functionalities.
    """

    def __init__(self):
        self.config = MailPilotConfig()
        self.mailer = MailPilot(self.config)

    def run(self):
        """
        Run the MailPilot Application.
        This method can be expanded to include CLI arguments, interactive mode etc.
        """
        self.mailer.run()

    def configure(self):
        """ Configure MailPilot settings """
        self.config.configure_interactively()

    def send_mail(self, subject, recipients, template):
        """ Send an email using the MailPilot """
        self.mailer.send_emails(subject, recipients, template)

    def update_config(self, **kwargs):
        """ Update configuration settings """
        self.config.update_settings(**kwargs)

# Example usage
def example_usage():
    app = MailPilotApplication()
    app.configure()
    app.run()

if __name__ == "__main__":
    example_usage()
