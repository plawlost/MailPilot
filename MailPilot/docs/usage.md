Usage Guide for MailPilot
---

MailPilot is a powerful tool for sending personalized emails. This guide covers basic and advanced usage.

## Basic Usage

### Sending an Email

To send an email using MailPilot, follow these steps:

1. **Prepare Your Recipient List:**
   Ensure your recipients' list is in a JSON format. For example:

   ```json
   [
       {"name": "John Doe", "email": "johndoe@example.com"},
       {"name": "Jane Smith", "email": "janesmith@example.com"}
   ]
   ```

2. **Write Your Email Template:**
   Create an HTML email template. Incorporate placeholders such as `{{name}}` for personalization.

3. **Send the Email:**
   Execute the following command:

   ```bash
   mailpilot send --template path/to/template.html --recipients path/to/recipients.json --subject "Your Email Subject"
   ```
   Replace the paths and subject with your actual template file, recipients file, and email subject.

## Advanced Usage

### Scheduling Emails

MailPilot can be integrated with scheduling tools like cron to send emails at specified intervals.

### Using MailPilot in Scripts

You can use MailPilot in your Python scripts by importing and utilizing its classes and functions.

### Help and Commands

For a list of all commands and options, run:

  ```bash
  mailpilot ---help
  ```
  