import discord
import youtube_dl
from discord.utils import get


async def ausfuehren(bot, nachricht, args):
    with youtube_dl.YoutubeDL({}) as ydl:
        song_info = ydl.extract_info(args[0], download=False)
        url = song_info["formats"][1]["url"]
        print(url)

    voice = get(bot.voice_clients, guild=nachricht.author.guild)
    voice.play(discord.FFmpegPCMAudio(url, before_options=" -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))
