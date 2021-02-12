import discord, json, os, requests, pathlib
from discord.utils import get
import youtube_dl
from pytube import YouTube

async def play(ctx, botObj, url):
    isSong = os.path.isfile("cmds/voice/audio_buffer/buffer.mp3")

    try:
        if isSong:
            os.remove("cmds/voice/audio_buffer/buffer.mp3")
    except PermissionError:
            await ctx.send('Unable to request song. (Song already in use.)')
            return

    await ctx.send('Preparing song. Please wait.')

    ytObj = YouTube(url)
    ytObj.streams.filter(only_audio=True).first().download("cmds/voice/audio_buffer")

    channel = ctx.message.author.voice.channel

    for file in os.listdir("cmds/voice/audio_buffer"):
        if file.endswith(".mp3") or file.endswith(".mp4"):
            os.rename("cmds/voice/audio_buffer/"+file, "cmds/voice/audio_buffer/buffer.mp3")

    voice_client: discord.VoiceClient = discord.utils.get(botObj.voice_clients, guild=ctx.guild)

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio('cmds/voice/audio_buffer/buffer.mp3'), after=None)
