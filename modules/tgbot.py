# import requests as requests
from datetime import datetime
from tzlocal import get_localzone
from telegram import Bot

url = "https://api.telegram.org/bot1075494982:AAGSzNNaCVvTrOvXjWPgw3kUPWMaGfwDmDU/"
token = "1075494982:AAGSzNNaCVvTrOvXjWPgw3kUPWMaGfwDmDU"
chat_id = '678954660'
tz = get_localzone()


def send_photo():
    today = datetime.now(tz).strftime("%I:%M%p on %B %d, %Y")
    bot = Bot(token=token)
    bot.send_photo(chat_id=chat_id, photo=open('last_captured_image.jpg', 'rb'), caption='Terdeteksi\n\n' + today)
