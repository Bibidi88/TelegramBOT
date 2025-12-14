import asyncio
import configparser
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest

CONFIG_FILE = "config.ini"
CHAT_ID_FILE = "chat_ids.txt"


def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename, encoding="utf-8")

    telegram = config["telegram"]
    api_id = telegram["api_id"]
    api_hash = telegram["api_hash"]

    return api_id, api_hash

async def main():

    api_id, api_hash = load_config(CONFIG_FILE)

    client = TelegramClient("session_name", api_id, api_hash)
    await client.start()

    contacts = await client(GetContactsRequest(hash=0))

    with open(CHAT_ID_FILE, "w", encoding="utf-8") as f:
        for user in contacts.users:
            name = user.first_name or "Kein Name"
            username = user.username or "None"
            f.write(f"{user.id}\n")

    await client.disconnect()
    print(f"✅ {CHAT_ID_FILE} wurde erstellt")

asyncio.run(main())
