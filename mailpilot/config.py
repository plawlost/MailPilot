# Copyright [2024] [Yağız Erkam '@plawlost' Çelebi]

import os
import json
import logging
from getpass import getpass
from configparser import ConfigParser

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MailPilotConfig:
    def __init__(self, config_file='mailpilot_config.ini'):
        self.config_file = config_file
        self.config = ConfigParser()
        self.load_config()

    def load_config(self):
        """ Load configuration from a file """
        if not os.path.exists(self.config_file):
            logging.info("Config file not found, creating new one.")
            self.create_default_config()
        else:
            self.config.read(self.config_file)

    def create_default_config(self):
        """ Create a default config file """
        self.config['SMTP'] = {
            'Host': '',
            'Port': 587,
            'User': '',
            'Password': ''
        }
        self.config['SETTINGS'] = {
            'Subject': 'Your Email Subject',
            'TemplatePath': 'email_template.html',
            'RecipientsPath': 'recipients.json'
        }
        self.save_config()

    def save_config(self):
        """ Save the current configuration to a file """
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def set_smtp_settings(self, host, port, user, password):
        """ Set SMTP server settings """
        self.config['SMTP']['Host'] = host
        self.config['SMTP']['Port'] = str(port)
        self.config['SMTP']['User'] = user
        self.config['SMTP']['Password'] = password
        self.save_config()

    def get_smtp_settings(self):
        """ Get SMTP server settings """
        return {
            'host': self.config.get('SMTP', 'Host'),
            'port': self.config.getint('SMTP', 'Port'),
            'user': self.config.get('SMTP', 'User'),
            'password': self.config.get('SMTP', 'Password')
        }

    def set_application_settings(self, subject, template_path, recipients_path):
        """ Set application specific settings """
        self.config['SETTINGS']['Subject'] = subject
        self.config['SETTINGS']['TemplatePath'] = template_path
        self.config['SETTINGS']['RecipientsPath'] = recipients_path
        self.save_config()

    def get_application_settings(self):
        """ Get application specific settings """
        return {
            'subject': self.config.get('SETTINGS', 'Subject'),
            'template_path': self.config.get('SETTINGS', 'TemplatePath'),
            'recipients_path': self.config.get('SETTINGS', 'RecipientsPath')
        }

    def configure_interactively(self):
        """ Interactive configuration setup """
        print("Enter your SMTP server details:")
        host = input("SMTP Host: ").strip()
        port = input("SMTP Port (default 587): ").strip() or 587
        user = input("SMTP User: ").strip()
        password = getpass("SMTP Password: ").strip()

        self.set_smtp_settings(host, port, user, password)

        print("\nConfigure application settings:")
        subject = input("Default Email Subject: ").strip()
        template_path = input("Path to Email Template: ").strip()
        recipients_path = input("Path to Recipients JSON file: ").strip()

        self.set_application_settings(subject, template_path, recipients_path)

        logging.info("Configuration saved successfully.")

# Example usage
if __name__ == "__main__":
    config = MailPilotConfig()
    config.configure_interactively()
