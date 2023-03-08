import discord


async def ausfuehren(bot, nachricht, args):
    print("Ping command wurde ausgeführt!")

    embed = discord.Embed(title="Pong", color=discord.Colour.green())

    await nachricht.channel.send(embed=embed)
    await nachricht.add_reaction("🐖")
