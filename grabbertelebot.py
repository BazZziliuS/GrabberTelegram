from telethon import TelegramClient, events
from telethon.tl.types import Channel
import asyncio
from config import settings

api_id = settings['api_key']
api_hash = settings['api_hash']

my_channel_id = -111111111
channels = [-1001166834860, -1001058912111, -1001009232144, -1001377397898, -1001006147755, -1001192361840, -1001125259868] # откуда пересылать
# -1001166834860 Ньюсач/Двач / -1001058912111 Рифмы и Панчи 🥤 / -1001006147755 MDK / -1001192361840 DarkSide
# -1001009232144 Двач / -1001377397898 Трусы Навального / -1001125259868 WebM
BADTEXT = {'t.me', 'http', 'подписаться', '@', 'joinchat', '#реклама', 'https', 'Olimpbet', '1xbet', 'TTC', 'подписывайтесь'} # исключения

client = TelegramClient('myGrab', api_id, api_hash)
print("Граббер запущен")

def to_lower(word: str):
    return word.lower()

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    global BADTEXT
    message_text_lowered = event.raw_text.lower()
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        if event.message and not event.grouped_id:
            await asyncio.sleep(1)
            await client.send_message(my_channel_id, event.message)

@client.on(events.Album(chats=channels))
async def handler(event):
    message_text_lowered = event.raw_text.lower()
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        await asyncio.sleep(1)
        await client.send_message(
            my_channel_id,
            file=event.messages,
            message=event.original_update.message.message,
        )

with client:
    client.run_until_disconnected()