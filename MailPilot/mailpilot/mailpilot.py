# Copyright [2024] [Yağız Erkam '@plawlost' Çelebi]

import argparse
import json
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_email(email):
    """ Validate email address format """
    pattern = r'[^@]+@[^@]+\.[^@]+'
    return re.match(pattern, email) is not None

def prompt_for_input(arg, prompt_message):
    """ Prompt for input if argument not provided """
    return arg if arg else input(prompt_message)

def load_recipients(recipients_file):
    """ Load recipients from a JSON file """
    try:
        with open(recipients_file, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading recipients: {e}")
        sys.exit(1)

def load_template(template_file):
    """ Load email template """
    try:
        with open(template_file, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error loading email template: {e}")
        sys.exit(1)

def send_emails(args, recipients, email_template):
    """ Send emails to the list of recipients """
    try:
        server = smtplib.SMTP(args.smtp_host, args.smtp_port)
        server.starttls()
        server.login(args.smtp_user, args.smtp_password)

        for recipient in recipients:
            if not validate_email(recipient['email']):
                logging.warning(f"Invalid email address: {recipient['email']}")
                continue

            msg = MIMEMultipart('alternative')
            msg['Subject'] = args.subject
            msg['From'] = args.smtp_user
            msg['To'] = recipient['email']

            html_content = email_template.replace("{{name}}", recipient['name'])
            msg.attach(MIMEText(html_content, 'html'))

            server.sendmail(args.smtp_user, recipient['email'], msg.as_string())
            logging.info(f"Email sent to {recipient['email']}")

        server.quit()
    except Exception as e:
        logging.error(f"Error sending emails: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="MailPilot - Automated Email Sender")
    parser.add_argument("--recipients", help="Path to JSON file with recipients")
    parser.add_argument("--template", help="Path to HTML email template")
    parser.add_argument("--smtp_host", help="SMTP server host")
    parser.add_argument("--smtp_port", type=int, default=587, help="SMTP server port")
    parser.add_argument("--smtp_user", help="SMTP username")
    parser.add_argument("--smtp_password", help="SMTP password")
    parser.add_argument("--subject", help="Email subject")

    args = parser.parse_args()

    args.recipients = prompt_for_input(args.recipients, "Enter path to recipients file: ")
    args.template = prompt_for_input(args.template, "Enter path to email template: ")
    args.smtp_host = prompt_for_input(args.smtp_host, "Enter SMTP host: ")
    args.smtp_port = int(prompt_for_input(args.smtp_port, "Enter SMTP port (default 587): "))
    args.smtp_user = prompt_for_input(args.smtp_user, "Enter SMTP user: ")
    args.smtp_password = prompt_for_input(args.smtp_password, "Enter SMTP password: ")
    args.subject = prompt_for_input(args.subject, "Enter email subject: ")

    recipients = load_recipients(args.recipients)
    email_template = load_template(args.template)

    send_emails(args, recipients, email_template)

if __name__ == "__main__":
    main()
