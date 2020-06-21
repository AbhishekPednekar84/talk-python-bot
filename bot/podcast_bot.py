import os
import requests
import dotenv

dotenv.load_dotenv()


class TalkPythonBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def get_updates(self, offset=None):
        url = self.base_url + "getUpdates?timeout=100"

        if offset:
            url = url + f"&offset={offset + 1}"
        r = requests.get(url)
        # print(url)
        return r.json()

    def send_message(self, msg, chat_id):
        url = (
            self.base_url
            + f"sendMessage?chat_id={chat_id}&text={msg}&parse_mode={'HTML'}&disable_web_page_preview={True}"
        )
        if msg:
            requests.get(url)
