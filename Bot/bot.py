import discord, os, sys, pathlib, base64, json, asyncio
from discord.ext import commands
from cogs import eventCog, commandCog

class Bot(object):

    def __init__(self, token="", command_prefix="ub."):
        self.token = token

        intents = discord.Intents.default() # Gets the default intents from discord.
        intents.members = True # enables members intents on the bot.
        intents.guilds = True
        intents.messages = True
        intents.dm_messages = True


        self.botObj = commands.Bot(command_prefix=command_prefix, help_command=None, intents=intents)


    def setup(self):
        self.botObj.add_cog(eventCog.Events(self.botObj))
        self.botObj.add_cog(commandCog.BotCommands(self.botObj))

    def run(self):
        self.botObj.run(self.token)
