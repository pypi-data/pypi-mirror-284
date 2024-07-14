# SendTextSMTP
A simple package to simplify the process to send text messages using the SMTP mail protocol.

## SETUP

You will need a app password if you are utilizing Gmail as your source email. 
Reference this help article: https://support.google.com/accounts/answer/185833?hl=en


## USAGE

### Import the module
  `import SendTextSMTP`

### Setting up the source email
  `messenger = SendTextSMTP.SMTP("YOUR_SOURCE_EMAIL", "YOUR_APP_PASSWORD", "YOUR_SMTP_SERVER", SMTP_PORT)`
  Using YOUR_SMTP_SERVER should look like `"smtp.gmail.com"` and SMTP_PORT `587` for gmail as an example.

### Sending a text message
  messenger.send_message("PHONE_NUMBER@CARRIER.COM", "MESSAGE")
  Note that for texts with multiple lines, you can use \r to indicate a newline.
