from mailpilot import MailPilotApplication, read_json_file

def main():
    # Initialize the MailPilot application
    app = MailPilotApplication()

    # Run configuration interactively (optional, can be skipped if already configured)
    # app.configure()

    # Example: Sending a single email
    subject = "Test Email from MailPilot"
    recipients = [{"name": "John Doe", "email": "johndoe@example.com"}]
    template = "<html><body><p>Hello {{name}},</p><p>This is a test email from MailPilot.</p></body></html>"

    app.send_mail(subject, recipients, template)

    # Example: Sending multiple emails using a recipients JSON file
    recipients_list = read_json_file('path_to_recipients.json')
    if recipients_list:
        app.send_mail("Newsletter", recipients_list, template)

if __name__ == "__main__":
    main()