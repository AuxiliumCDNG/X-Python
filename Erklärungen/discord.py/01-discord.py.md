# Discord.py als API-Wrapper
Ein API-Wrapper mach die Funktionen einer API für den Programmierer besser zugänglich, indem die Schnittstellen durch eine Klasse verpackt werden und nützliche Operationen erhalten, sodass die Arbeit mit den Daten vereinfacht wird.
Ein API-Wrapper enthält auch Operationen, die Daten zur API senden, ohne dass man selbst eine Anfrage zusammenbauen muss, das übernimmt der API-Wrapper.

---

Um discord.py zu verwenden, muss man die Bibliothek installieren:

Über den Paketmanager:
```bash
pip install discord.py
```

Oder über PyCharm: `File -> Settings -> Project -> Interpreter`

Wie jeder Bot braucht auch discord.py einen Token, um sich bei der Discord API zu authentifizieren. Diesen muss man sich über die Discord Entwicklerseite erstellen:
<https://discord.com/developers/applications>

Ggf. Bot erstellen und Namen bestätigen.

Dann Token direkt kopieren und abspeichern. Falls dieser nicht angezeigt wird, muss der Token über "reset Token" zurückgesetzt werden. Dann wird er wieder einmalig angezeigt.

---

Man beginnt damit, eine Client-Instanz zu erstellen. Diese kümmert sich um die Grundfunktionen des Bots. Sie enthält Operationen, um den Bot zu starten und ihn anzumelden etc. Sie kümmert sich auch um Events:

```python
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot ist bereit!')

client.run('TOKEN')

```

Damit der Bot auf Nachrichten reagiert, muss man ein "on_message" Event erstellen. Die zugehörige Funktion wird immer dann ausgeführt, wenn der Bot auf einem belibiegen Weg eine neue Nachricht sieht.

```python
@client.event
async def on_message(nachricht):
    # Der Bot soll nicht auf seine eigenen Nachrichten reagieren.
    if nachricht.author.id == bot.user.id:
        return
    # Der Bot soll nicht auf Nachrichten reagieren, die ihm privat geschrieben werden.
    if nachricht.channel is discord.DMChannel:
        return

    # Der Bot soll Nachrichten ignorieren, die nicht mit dem Prefix beginnen.
    prefix = "!"  # Hier kann eine beliebige Zeichenkette verwendet werden.
    if not str(nachricht.content).startswith(prefix):
        return

    ...
```

Damit man verschiedene Commands implementieren kann, muss die Nachricht geparsed (verarbeitet) werden, um den richtigen Command auszuführen.

Dies passiert in diesem Beispiel in einigen Schritten:

```python
worte = nachricht.content.split(" ")  # Die Nachricht in einzelne Worte zerlegen.

befehl = worte[0][len(prefix):]  # Das erste Wort für den Commandnamen verwenden und den Prefix vorne entfernen.
args = worte[1:]  # Die Argumente sind die folgenden Worte.
```

Um Strings und Listen zu parsen wird in Python häufig mit einer Syntax gearbeitet, die ca. so aussieht: `text[3:6]`<br>
Wie diese im Einzelnen funktioniert ist nicht wichtig und hier vorgegeben. Wichtig ist nur, dass das erste Wort der Namen des Befehls ist (als String in befehl) und das folgenden die Argumente (als Liste in args).

Der Command soll nun ausgeführt werden:

```python
# Die Datei/das Modul, dass den Namen des Befehls trägt wird aus dem Ordner "bot_befehle" importiert.
befehl_modul = importlib.import_module("bot_befehle."+befehl)
# Vom Modul wird die Funktion "ausfuehren" geholt, die jeder Bot Command haben muss.
befehl_funktion = getattr(befehl_modul, "ausfuehren")
# Diese Funktion wird mit await und den entsprechenden Parametern ausgeführt.
await befehl_funktion(bot, nachricht, args)
```

Damit wäre das Gerüst des Bots abgeschlossen!