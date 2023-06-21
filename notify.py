import telebot
import json
import requests

with open(".config_notify.json", "r") as tokens:
    data = json.load(tokens)

bot_token = data["bot_token"]
bot_chatID = data["bot_chatID"]

bot = telebot.TeleBot(bot_token) # conecta com o bot pela chave


def send_notification(message):
    bot.send_message(chat_id=bot_chatID, text=message)

def handle_send_notificationVerbose(message):
    send_notification(message)
    # Verifica se a mensagem foi enviada corretamente
    if message is not None:
        return 'Notification sent successfully!'
    else:
        return 'Failed to send notification.', 400
    
def handle_send_notification(message):
    send_notification(message)
    return '', 204

