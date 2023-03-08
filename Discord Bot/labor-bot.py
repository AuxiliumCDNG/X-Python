import discord
import importlib
import config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Ich bin fertig!")

@bot.event
async def on_message(nachricht):
    if nachricht.author.id == bot.user.id:
        return

    if nachricht.channel is discord.DMChannel:
        return

    prefix = "!"

    if not str(nachricht.content).startswith(prefix):
        return

    befehl = str(nachricht.content).split(" ")[0][len(prefix):]
    print(befehl)
    args = str(nachricht.content).split(" ")[1:]
    print(args)

    befehl_modul = importlib.import_module("bot_befehle."+befehl)
    befehl_funktion = getattr(befehl_modul, "ausfuehren")
    await befehl_funktion(bot, nachricht, args)

@bot.event
async def on_presence_update(before, after):
    print("Jemand hat etwas getan yay")

    print(before.activity.name, "->", after.activity.name)

bot.run(config.discord_key)
