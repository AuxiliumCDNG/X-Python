import random

import discord
import requests


async def ausfuehren(bot, nachricht, args):
    suchbegriff = " ".join(args)
    bild_suche = requests.get(f"https://api.unsplash.com/search/photos?per_page=30&query={suchbegriff}&client_id=Aa35vpOYaE6-vcujz40rOmifzouYw-0HDTNuEGuM9ug").json()

    print(bild_suche)

    if bild_suche["total"] == 0:
        await nachricht.channel.send("Kein Bild gefunden!")
        return
    elif bild_suche["total"] < 30:
        anzahl = bild_suche["total"]
    else:
        anzahl = 30

    index = random.randint(0, anzahl-1)

    bild_url = bild_suche["results"][index]["urls"]["regular"]

    embed = discord.Embed(title="Bild", color=discord.Colour.green())
    embed.set_image(url=bild_url)

    await nachricht.channel.send(embed=embed)
