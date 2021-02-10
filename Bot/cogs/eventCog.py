import discord, requests, json, asyncio
from discord.ext import commands
from cmds import welcome

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await welcome.welcome(member, self.bot)

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        await member.send("Did ya leave accidentally?")
        await member.send("`To rejoin the UnderDog world use: https://discord.gg/mAKCtWjpUU`")
