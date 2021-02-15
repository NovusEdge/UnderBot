import discord, json, os, pathlib, requests
import validators
from discord.utils import get
from cmds.voice.youtube import youtube_handle as yt_handle
from cmds.voice.spotify import spotify_handle as spt_handle

DOMAINS = {
    "youtube.com": yt_handle.play,
    "youtu.be": yt_handle.play,
    "spotify.com": spt_handle.play
}

async def play(ctx, botObj, url):
    for i in DOMAINS:
        if i in url:
            await DOMAINS[i](ctx, botObj, url)
            return
