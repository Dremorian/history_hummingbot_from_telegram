import asyncio
import uvicorn
from fastapi import FastAPI
from telethon import TelegramClient, events, utils, sync
import time
from dotenv import load_dotenv
import os

# For async, not worked with uvicorn or need to know how
# api_id = int(os.environ.get("api_id"))
# api_hash = os.environ.get("api_hash")
# client = TelegramClient('test', api_id, api_hash)

app = FastAPI()


@app.get("/history")
def make_response():
    load_dotenv()
    api_id = int(os.environ.get("api_id"))
    api_hash = os.environ.get("api_hash")
    chat = os.environ.get("chat")
    asyncio.set_event_loop(asyncio.new_event_loop())
    client = TelegramClient('test', api_id, api_hash)
    client.start()
    # init all chats to session - without it first time don't work client.send_message(chat, 'history')
    dialogs = client.iter_dialogs()
    # Send message "history"
    client.send_message(chat, 'history')
    id_mes = 0
    # Take id last message "history"
    for message in client.iter_messages(chat):
        if message.text == 'history':
            id_mes = message.id
            print(id_mes)
        break
    # wait to take answer hummingbot to telegramm chat
    time.sleep(15)
    # take messages after message history
    history = []
    for message in client.iter_messages(chat, reverse=True):
        if message.id > id_mes:
            history.append(message.text)
    # history = "".join(history)
    client.disconnect()
    return history

# async version
# async def history():
#     chat = os.environ.get("chat")
#     await client.send_message(chat, 'history')
#     id_mes = 0
#     async for message in client.iter_messages(chat):
#         if message.text == 'history':
#             id_mes = message.id
#             print(id_mes)
#         break
#     await asyncio.sleep(15)
#     # async for message in client.iter_messages('HammingDev', from_user='HammingDev'):
#     history = []
#     async for message in client.iter_messages(chat, reverse=True):
#         if message.id > id_mes:
#             print(message.id, message.text)
#             # history += message.text
#             history.extend(message.text)
#     # history = "".join(history)
#     return history


if __name__ == "__main__":
    uvicorn.run("server:app",
                host="0.0.0.0",
                port=9400,
                )