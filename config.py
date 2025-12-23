import os

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

EMAIL_FROM = os.getenv("SMTP_USERNAME")
EMAIL_TO = os.getenv("SMTP_TO")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")

PRODUCT_URL = os.getenv("PRODUCT_URL")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

# CSS selector that ONLY exists when product is available
AVAILABILITY_SELECTOR = "Disponibilidade estimada"

STATE_FILE = "state.json"

EMAIL_ENABLED = True

