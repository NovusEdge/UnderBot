import discord, requests, json, asyncio
from discord.ext import commands
from cmds import help, invite, get_cat, get_dog, get_kawaii, set_pre, welcome
from cmds.voice import join_vc


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(aliases=["setpre", "set_prefix"])
    async def setprefix(self, ctx):
        await set_pre.setprefix(ctx, self.bot)

    @commands.command(aliases=["resetpre", "reset_prefix"])
    async def resetprefix(self, ctx):
        self.bot.command_prefix = "ub."
        await ctx.send("`Command Prefix` set to default: `ub.`")
