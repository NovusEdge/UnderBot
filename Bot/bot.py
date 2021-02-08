import discord, os, sys, pathlib, base64, json, asyncio
from discord.ext import commands
from cogs import eventCog

class Bot(object):

    def __init__(self, token="", command_prefix="ub."):
        self.token = token
        self.botObj = commands.Bot(command_prefix=command_prefix, help_command=None)

    def setup(self):
        self.botObj.add_cog(eventCog.Events(self.botObj))

    def run(self):
        self.botObj.run(self.token)
