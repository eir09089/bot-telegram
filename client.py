
from telethon import TelegramClient, sync
from  telethon.tl.types import UpdateNewChannelMessage
from handler import *
from api import *
import pprint

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

api_id =  ''
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)
# client.session.close()
# client.start()



# def get_env(name, message, cast=str):
#     import os
#     import sys
#     import time
#     if name in os.environ:
#         return os.environ[name]
#     while True:
#         value = input(message)
#         try:
#             return cast(value)
#         except ValueError as e:
#             print(e, file=sys.stderr)
#             time.sleep(1)



async def update_handler(update):
    if isinstance(update, UpdateNewChannelMessage):
        print(update)
        print(update.to_dict()['message']['message'])
        text = update.to_dict()['message']['message']
        answer = extractInfo(text)
        print(answer)
        # sendEmail(formatResponse(answer))

        # print(update.to_dict()['message']['to_id']['channel_id'])
        # print(update.to_dict()['message']['media'])



client.add_event_handler(update_handler)

'''You could also have used the @client.on(...) syntax:
from telethon import events
@client.on(events.Raw)
async def update_handler(update):
    print(update)
'''

with client.start():
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()