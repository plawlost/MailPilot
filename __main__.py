# mailpilot/__main__.py

import argparse
from .mailpilot import send_emails, load_recipients, load_template
from .config import MailPilotConfig

def main():
    parser = argparse.ArgumentParser(description="MailPilot - Automated Email Sender")

    # Configuring Subparsers for different functionalities
    subparsers = parser.add_subparsers(dest="command")
    
    # Subparser for sending emails
    send_parser = subparsers.add_parser("send", help="Send emails")
    send_parser.add_argument("--recipients", help="Path to JSON file with recipients", required=True)
    send_parser.add_argument("--template", help="Path to HTML email template", required=True)
    send_parser.add_argument("--subject", help="Email subject", required=True)

    # Subparser for configuring SMTP settings
    config_parser = subparsers.add_parser("configure", help="Configure MailPilot settings")
    config_parser.add_argument("--smtp_host", help="SMTP server host", required=True)
    config_parser.add_argument("--smtp_port", type=int, default=587, help="SMTP server port")
    config_parser.add_argument("--smtp_user", help="SMTP username", required=True)
    config_parser.add_argument("--smtp_password", help="SMTP password", required=True)
    
    # Parse the arguments
    args = parser.parse_args()

    # Handling commands
    if args.command == "send":
        recipients = load_recipients(args.recipients)
        email_template = load_template(args.template)
        send_emails(args, recipients, email_template)

    elif args.command == "configure":
        config = MailPilotConfig()
        config.set_smtp_settings(args.smtp_host, args.smtp_port, args.smtp_user, args.smtp_password)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
