from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler, MessageHandler, Filters
from test_regex import  *

updater = Updater(token='')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def formatResponse(info):
    email = 'SPORT: {0}\nEVENT: {3}\nBET: {4} \nODDS: {1}\nSTAKE: {2}\nBOOK: bet365'.format(*info)
    return email

def sendEmail(info):
    import smtplib
    # from smtplib.email.MIMEMultipart import MIMEMultipart
    from email import MIMEMultipart
    from email import MIMEText

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()


    fromaddr = ""
    toaddr = ""
    msg = MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Hello world"

    body = formatResponse(info)
    msg.attach(MIMEText.MIMEText(body, 'plain'))

    server.login(fromaddr, "")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def echo(bot, update):
    answer = extractInfo(update.message.text)
    # print formatResponse(answer)
    sendEmail(answer)
    bot.send_message(chat_id=update.message.chat_id, text=answer)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def extract_text(bot, update):
    photo = update.message.photo
    for pic in photo:
        bot.send_message(chat_id=update.message.chat_id, text='Got an image ' + pic.file_id)

photo_handler = MessageHandler(Filters.photo, extract_text)
dispatcher.add_handler(photo_handler)