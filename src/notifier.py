import requests
from user_registry import get_chat_id

BOT_TOKEN = "8749729067:AAEWEbuj0B0MXa5Ed_Wbyl3JW_p18s9Tn2c"

def send_alert(phone, message):

    chat_id = get_chat_id(phone)

    if not chat_id:
        print("User not registered for alerts")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
