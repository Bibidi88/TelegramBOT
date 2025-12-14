# TelegramBOT
Telegram Bot to send Messages


Schritt-für-Schritt-Anleitung

installiere Python auf deinem PC aktuell 3.14.0
1. https://www.python.org/downloads/
2. folge dem installer


Erstell eine API_ID & API_HASH
1. https://my.telegram.org
2. Login
3. API development tools
4. Denk dir irgend ein Namen und kurz Namen aus lass den rest leer.
5. Kopieren Sie diesen langen Code und speichern Sie ihn sicher in der config.ini unter API_ID und API_HASH ab.


Erstelle einen TelegramBot
1. Starten Sie die Telegram-App auf Ihrem Gerät.
2. Suchen Sie @BotFather: Nutzen Sie die Suchfunktion und suchen Sie nach @BotFather (achten Sie auf das verifizierte Häkchen).
3. Starten Sie den Bot: Tippen Sie auf „Starten“ oder senden Sie den Befehl /start.
4. Erstellen Sie einen neuen Bot: Senden Sie den Befehl /newbot.
5. Geben Sie einen Namen ein: Wählen Sie einen Namen für Ihren Bot (z.B. „MeinSuperBot“).
6. Wählen Sie einen Benutzernamen: Legen Sie einen eindeutigen Benutzernamen fest, der mit dem Wort „bot“ enden muss (z.B. MeinSuper_bot).
7. Speichern Sie das Token: Der BotFather gibt Ihnen ein BOT-Token. Kopieren Sie diesen langen Code und speichern Sie ihn sicher in der config.ini unter TOKEN ab.


Installiere die Abhängigkeiten für den bot (requests & telethon)
1. Öffne dein Terminal (CMD) in dem Ordner wo du den bot gespeichert hast und schreibe
2. pip install requests
3. pip install telethon


Starte hole die IDS von deinen Freunden
1. Öffne dein Terminal (CMD) in dem Ordner wo du den bot gespeichert hast und schreibe
2. python ids.py
3. schreibe deine Telefonnummer (+4912345678901) wichtig mit Vorwahl.
4. du solltest einen code per Telegramm bekommen schreibe diesen nun hier rein.
5. Die ids sollten nun in der chat_ids.txt gespeichert sein


Passe deine Nachricht an.
1. Öffne config.ini
2. hinter message scheibe deine Nachricht


Starte den bot dieser sendet nun automatisch deine Nachricht an die IDS aus der chat_ids.txt
1. Öffne dein Terminal (CMD) in dem Ordner wo du den bot gespeichert hast und schreibe
2. python bot.py

wenn du fragen hast fuck you you didnt pay for it
