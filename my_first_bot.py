from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler, MessageHandler, Filters

updater = Updater(token='676190340:AAF69uHq5uaM6NDIQkbLYWxjGOFy8EtOLOw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
