import telebot
from PIL.ImageStat import Global
from lxml.html.diff import token

token = '7581581367:AAEfvQRx9i8_L-D-13nJSpjhxWkuaE5-jEs'

bot = telebot.TeleBot(token)

Name = 'Вася'

@bot.message_handler(content_types=["text"])
def echo(message):
    if Name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)