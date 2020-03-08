import requests as requests



url = "https://api.telegram.org/bot1075494982:AAGSzNNaCVvTrOvXjWPgw3kUPWMaGfwDmDU/"


def send_message( text):
    chat = ['678954660']
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url+'sendMessage', data=params)
    return response