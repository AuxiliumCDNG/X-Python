import asyncio

from discord.utils import get


async def ausfuehren(bot, nachricht, args):
    voice = await nachricht.author.voice.channel.connect()

