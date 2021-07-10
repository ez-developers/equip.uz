
import requests
from time import time
from dotenv import load_dotenv
from backend.settings import SMS_API_URL
import os

load_dotenv()


def send_sms(recipient: int,
             text: str):
    """
    Recipient length: 12 chararcters
    """

    headers = {'Content-type': 'application/json',
               'Authorization': f'Basic {os.getenv("SMS_API_TOKEN")}'}
    data = {
        "messages":
            [
                {
                    "recipient": f"{str(recipient)}",
                    "message-id": f"{int(time() * 1000000)}",

                    "sms": {

                        "originator": "3700",
                        "content": {
                            "text": f"{text}"
                        }
                    }
                }
            ]
    }

    return requests.post(SMS_API_URL, json=data, headers=headers)


def sms_text(code: int):
    return f'Ваш код регистрации для "Equip" - {code}. Введите его в телеграм бот.'
