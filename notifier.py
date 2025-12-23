import smtplib
import ssl
from email.message import EmailMessage
from config import (
    EMAIL_ENABLED,
    SMTP_HOST,
    SMTP_PORT,
    EMAIL_FROM,
    EMAIL_TO,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    PRODUCT_URL
)

def send_notification():
    if not EMAIL_ENABLED:
        return

    msg = EmailMessage()
    msg["Subject"] = "🚨 Product Available"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    msg.set_content(
        "Good news!\n\n"
        "The product you are monitoring is now AVAILABLE.\n\n"
        "Check it as soon as possible before it sells out."
        f"The product is available!\n\n{PRODUCT_URL}"
    )

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            print(f"SMTP login successful")
            server.send_message(msg)

        print("Email notification sent successfully")

    except Exception as e:
        print(f"Failed to send email: {e}")

send_notification()