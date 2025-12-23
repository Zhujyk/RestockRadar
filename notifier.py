import smtplib
import ssl
from email.message import EmailMessage
from config import SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO, EMAIL_ENABLED, PRODUCT_URL

def send_notification():
    if not EMAIL_ENABLED:
        return

    msg = EmailMessage()
    msg["Subject"] = "🚨 Product Available"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(f"Good news! The product at {PRODUCT_URL} is now available!")

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print("Email notification sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
