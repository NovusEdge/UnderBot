import discord, json, os, requests
from discord.utils import get


async def join(ctx):
    channel = ctx.author.voice.channel
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()
