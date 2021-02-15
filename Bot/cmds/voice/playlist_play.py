import discord, json
from discord.utils import get
from pytube import YouTube
from cmds.voice import play_aud as aud_base

async def play(ctx, botObj):
    with open("cmds/voice/audio_buffer/queue.json", "r") as f:
        urls = json.load(f)["urls"]

    if len(urls) == 0:
        await ctx.send("No songs/audio in playlist.\nAdd em using: `[prefix]add [yt_url]`")
        return

    voice_client: discord.VoiceClient = discord.utils.get(botObj.voice_clients, guild=ctx.guild)

    for i in urls:
        await _play_one(ctx, botObj, i)


async def _play_one(ctx, botObj, url):
    await ctx.send(f"Now playing: {url}")
    await aud_base.play(ctx, botObj, url)
