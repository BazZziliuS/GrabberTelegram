from telethon import TelegramClient, events
from telethon.tl.types import Channel
import asyncio
from config import settings
import datetime

api_id = settings['api_key']
api_hash = settings['api_hash']

my_channel_id = -1001745238211
channels = [-1001166834860, -1001058912111, -1001377397898, -1001006147755, -1001075039748] # откуда пересылать
# onlyvideochannel = [-1001159691595, -1001192361840, -1001240524277] # от куда пересылать только видео
# -1001166834860 Ньюсач/Двач / -1001058912111 Рифмы и Панчи 🥤 / -1001192361840 DarkSide / -1001240524277 Неадекват
# -1001377397898 Трусы Навального / -1001125259868 WebM / -1001006147755 MDK / -1001159691595 Джокер / -1001075039748 Мурзилка
BADTEXT = {'t.me', 'http', 'подписаться', '@', 'joinchat', '#реклама', 'https', 'Olimpbet', '1xbet', 'TTC', 'подписывайтесь', 'подпишитесь', 'эмигрицепс', 'MDK', 'SHOT', 'Человек Разумный', 'projecthomosapiens', 'UVcSZMPTP9s2ZjQy', '👉 Рифмы и Панчи](https://t.me/rhymestg)', '[👉 Рифмы и Панчи 18+](https://t.me/rhymestg)', '👉', 'inside zero', 'Ⓘ', '[Трусы Навального](https://t.me/+tcitCI78ECEzZjRi)', 'Трусы Навального', 'Подпишись', '⚡️Читать', '[Трусы Навального](https://t.me/+tcitCI78ECEzZjRi)👈🏻', 'ft.com', 'Трусы Навального👈🏻', '[MDK.txt](https://t.me/+oqFkBNJwXKljM2Zi)', 'MDK.txt' , 'https://t.me/+oqFkBNJwXKljM2Zi'} # исключения

client = TelegramClient('myGrab', api_id, api_hash)
print("Граббер запущен "+datetime.datetime.today().strftime("%d/%m/%Y-%H.%M.%S"))

def to_lower(word: str):
    return word.lower()

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    global BADTEXT
    message_text_lowered = event.raw_text.lower()
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        if event.message and not event.grouped_id:
            await asyncio.sleep(0.5)
            await client.send_message(my_channel_id, event.message)
            print('Заграбили пост '+datetime.datetime.today().strftime("%d/%m/%Y-%H.%M.%S ")+ event.message.message)

@client.on(events.Album(chats=channels))
async def handler(event):
    message_text_lowered = event.raw_text.lower()
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        await asyncio.sleep(0.5)
        await client.send_message(
            my_channel_id,
            file=event.messages,
            message=event.original_update.message.message,
        )
        print('Заграбили Альбом '+datetime.datetime.today().strftime("%d/%m/%Y-%H.%M.%S ") + event.original_update.message.message)


# @client.on(events.NewMessage(chats=onlyvideochannel))
# async def fsdaevent_handler(event):
#     message_text_lowered = event.raw_text.lower()
#     if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
#         await asyncio.sleep(1)
#         await client.send_file(my_channel_id, file=event.message, caption="@FreekNews 👈")
#         print('Заграбили Видео '+datetime.datetime.today().strftime("%d/%m/%Y-%H.%M.%S"))


with client:
    client.run_until_disconnected()
