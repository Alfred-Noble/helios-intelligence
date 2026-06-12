import smtplib
import os

from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()


class EmailService:

    @staticmethod
    def send_email(
        recipient: str,
        subject: str,
        body: str
    ):

        sender_email = os.getenv("EMAIL_USER")
        app_password = os.getenv("EMAIL_PASSWORD")

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:

            server.starttls()

            server.login(
                sender_email,
                app_password
            )

            server.send_message(msg)

        return {
            "status": "sent",
            "recipient": recipient
        }