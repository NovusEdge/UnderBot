import discord, requests, json, asyncio
from discord.ext import commands
from cmds import help, invite, welcome, get_cat, get_dog, get_kawaii

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.command(aliases=["h", "HELP", "Help"])
    async def help(self, ctx):
        await help.help(ctx)

    @commands.command(aliases=["INVITE", "Invite"])
    async def invite(self, ctx):
        await invite.invite(ctx)

    @commands.command(aliases=["CATS","cat","CAT"])
    async def cats(self, ctx):
        await get_cat.cats(ctx)

    @commands.command(aliases=["DOGS","DOG","dog"])
    async def dogs(self, ctx):
        await get_dog.dogs(ctx)

    @commands.command(aliases=["KAWAII", "cute", "Kawaii"])
    async def kawaii(self, ctx):
        await get_kawaii.kawaii(ctx)

    @commands.command(aliases=["wlcm", "welcome"])
    async def welcome_command(self, ctx):
        await welcome.welcome_command(ctx)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await welcome.welcome(member, self.bot)
