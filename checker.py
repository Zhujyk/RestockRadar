import requests
from bs4 import BeautifulSoup
from config import PRODUCT_URL, HEADERS, AVAILABILITY_SELECTOR


def is_product_available() -> bool:
    response = requests.get(
        PRODUCT_URL,
        headers=HEADERS,
        timeout=15,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for text_node in soup.stripped_strings:
        text = text_node.lower()
        if text.startswith(AVAILABILITY_SELECTOR.lower()):
            print(f"Is not available!")
            return False

    print("Is available!")
    return True
    
