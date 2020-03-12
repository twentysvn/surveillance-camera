import requests as requests
from telegram import Bot

url = "https://api.telegram.org/bot1075494982:AAGSzNNaCVvTrOvXjWPgw3kUPWMaGfwDmDU/"
token = "1075494982:AAGSzNNaCVvTrOvXjWPgw3kUPWMaGfwDmDU"
chat = ['678954660']


def send_message(text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def send_photo():
    bot = Bot(token=token)
    bot.send_photo(chat_id=chat, photo=open('saved_img.jpg', 'rb'))
