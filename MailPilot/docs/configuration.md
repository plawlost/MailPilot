Configuration Guide for MailPilot
---

MailPilot requires some initial configuration to set up SMTP settings and other options. Follow these steps to configure MailPilot.

### Configuring SMTP Settings

1. **Access Configuration:**
   After installing MailPilot, run the configuration command and provide SMTP details directly as command-line arguments:

   ```bash
   mailpilot configure --smtp-host smtp.yourmailserver.com --smtp-port 587 --smtp-user your-email@example.com --smtp-password your-password
   ```

   Replace the placeholders with your actual SMTP details.

### Configuring Email Templates and Recipients

- Place your email templates and recipient JSON files in a known directory.
- You can specify the default paths for these files in the command-line arguments or use environment variables.

### Saving Configuration

After entering all details, the configuration will be saved and used for future email sending operations.

### Advanced Configuration

For advanced users, MailPilot supports editing the configuration directly by passing arguments. Alternatively, you can set environment variables with your configuration details.

- **SMTP Host:** `MAILPILOT_SMTP_HOST`
- **SMTP Port:** `MAILPILOT_SMTP_PORT`
- **SMTP User:** `MAILPILOT_SMTP_USER`
- **SMTP Password:** `MAILPILOT_SMTP_PASSWORD`

Here's an example of setting environment variables:

  ```bash
  export MAILPILOT_SMTP_HOST=smtp.yourmailserver.com
  export MAILPILOT_SMTP_PORT=587
  export MAILPILOT_SMTP_USER=your-email@example.com
  export MAILPILOT_SMTP_PASSWORD=your-password
  ```