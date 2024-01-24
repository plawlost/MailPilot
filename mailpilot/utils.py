# Copyright [2024] [Yağız Erkam '@plawlost' Çelebi]

import re
import logging
import os
from email.utils import parseaddr
from typing import Tuple

# Configure logging
def setup_logging(level=logging.INFO):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_email(email: str) -> bool:
    """ Validate an email address for correct format """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def extract_name_email(address: str) -> Tuple[str, str]:
    """ Extract name and email from an address """
    name, email = parseaddr(address)
    return name.strip(), email.strip()

def file_exists(filepath: str) -> bool:
    """ Check if a file exists at the given path """
    return os.path.isfile(filepath)

def create_if_not_exists(filepath: str):
    """ Create a file if it does not exist """
    if not file_exists(filepath):
        with open(filepath, 'w') as file:
            file.write('')

def validate_file_path(filepath: str, file_description: str) -> bool:
    """ Validate if the given file path exists and log error if not """
    if not file_exists(filepath):
        logging.error(f'{file_description} file not found at {filepath}')
        return False
    return True

def prompt_for_input(prompt_message: str, default_value=None) -> str:
    """ Prompt for user input with an optional default value """
    user_input = input(prompt_message)
    return user_input.strip() if user_input else default_value

def secure_input(prompt_message: str) -> str:
    """ Securely capture sensitive user input """
    try:
        from getpass import getpass
        return getpass(prompt_message)
    except Exception as e:
        logging.error(f"Error in secure input: {e}")
        return prompt_for_input(prompt_message)

def read_json_file(filepath: str):
    """ Read a JSON file and return its contents """
    try:
        import json
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f'Error decoding JSON from {filepath}: {e}')
    except Exception as e:
        logging.error(f'Error reading file {filepath}: {e}')
    return None

def write_json_file(filepath: str, data):
    """ Write data to a JSON file """
    try:
        import json
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f'Error writing to file {filepath}: {e}')

# Example of using setup_logging
if __name__ == "__main__":
    setup_logging()
    email = "example@example.com"
    if validate_email(email):
        logging.info(f"{email} is a valid email address")
    else:
        logging.error(f"{email} is not a valid email address")
