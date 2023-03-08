from discord.utils import get


async def ausfuehren(bot, nachricht, args):
    voice = get(bot.voice_clients, guild=nachricht.author.guild)
    await voice.disconnect()
