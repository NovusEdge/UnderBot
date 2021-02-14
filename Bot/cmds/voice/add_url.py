import discord, json, os, requests, pathlib
from discord.utils import get

async def add(url):
    with open("cmds/voice/audio_buffer/queue.json", "r") as f:
        data = json.load(f)

    data["urls"].append(url)

    with open("cmds/voice/audio_buffer/queue.json", "w") as f:
        json.dump(data, f)
