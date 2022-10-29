import requests


class TelegramMessage:
    def __init__(self, token, chat_id):
        self.bot_token = token
        self.bot_chatid = chat_id

    def telegram_bot_sendtext(self, bot_message):
        send_text = "https://api.telegram.org/bot" + self.bot_token + "/sendMessage?chat_id=" + self.bot_chatid + \
                    "&parse_mode=Markdown&text=" + bot_message
        requests.get(send_text)
