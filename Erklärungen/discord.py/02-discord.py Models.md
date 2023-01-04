# discord.py Models

Models sind Klassen, die von Discord.py verwendet werden, um API Daten zu repräsentieren. Es gibt eigenen Klassen für fast jeden Datensatz, den die Discord API liefert.

Es folgt eine kleine Übersicht der Models, die am wichtigsten sind mit deren wichtigsten Methoden und Attributen. Diese und weitere sind auch in der offiziellen Dokumentation zu finden: <https://discordpy.readthedocs.io/en/stable/api.html#discord-models>

## Übersicht

### Nachricht
Attribute:

* author - Der Author der Nachricht (Member Model)
* content - Der Inhalt der Nachricht
* channel - Der Channel, in dem die Nachricht geschrieben wurde (TextChannel Model)

Methoden:

* `await delete()` - Löscht diese Nachricht
* `await edit("NEUER TEXT")`
* `await reply("TEXT")` - Antwortet auf eine Nachricht


## Channel
Attribute:

* name - Name des Kanals
* guild - Server auf dem der Kanal ist (Guild Model)

Methoden:

* `await send("TEXT")` - Sendet eine Nachricht in diesen Channel
* `await purge(limit=anzahl)` - Lösche eine Anzahl von Nachrichten aus dem Channel


...weiteres folgt