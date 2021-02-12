import discord, requests, json, asyncio
from discord.ext import commands
from cmds import welcome, set_wlcm

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel = None

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await welcome.welcome(member, self.bot)
        if self.welcome_channel is not None:
            await welcome.welcome_command(self.welcome_channel, member)

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        await member.send("Did ya leave accidentally?")
        await member.send("`To rejoin the UnderDog world use: https://discord.gg/mAKCtWjpUU`")

    @commands.command(aliases=["setwlcm", "wlcm_chan"])
    async def set_welcome_channel(self, ctx):
        self.welcome_channel = ctx
        await set_wlcm.set_welcome_channel(ctx, self.bot, self.welcome_channel)
