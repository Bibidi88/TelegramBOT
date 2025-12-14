import requests
import time
import configparser

CONFIG_FILE = "config.ini"
CHAT_ID_FILE = "chat_ids.txt"

def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename, encoding="utf-8")

    telegram = config["telegram"]
    token = telegram["token"]
    pause = float(telegram.get("pause_seconds", 0))
    message = telegram["message"]

    return token, pause, message


def load_chat_ids(filename):
    chat_ids = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                chat_ids.append(int(line))
    return chat_ids


def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload, timeout=10)
    return response.json()


def main():
    token, pause, message = load_config(CONFIG_FILE)
    chat_ids = load_chat_ids(CHAT_ID_FILE)

    print(f"✅ token = {token}")
    print(f"✅ pause = {pause} Sekunden")
    print(f"✅ message = {message}")

    for chat_id in chat_ids:
        result = send_message(token, chat_id, message)

        if result.get("ok"):
            print(f"✅ Gesendet an {chat_id}")
        else:
            print(f"❌ Fehler bei {chat_id}: {result}")

        if pause > 0:
            time.sleep(pause)


if __name__ == "__main__":
    main()
