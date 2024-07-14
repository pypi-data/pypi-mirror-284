import smtplib


class SMTP:
    def __init__(self, email, password, smtp_server, port):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port

    def send_message(self, recipient, message) -> None:
        auth = (self.email, self.password)
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login(auth[0], auth[1])
        server.sendmail(auth[0], recipient, message)
