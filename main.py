import telebot
from lxml.html.diff import token

token = '7581581367:AAEfvQRx9i8_L-D-13nJSpjhxWkuaE5-jEs'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)