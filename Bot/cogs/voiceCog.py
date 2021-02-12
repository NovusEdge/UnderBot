from cmds.voice import join_vc, play_aud
import discord, requests, json, asyncio
from discord.ext import commands
from discord.utils import get

class Voices(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["join_vc", "vc", "join"])
    async def join_voice(self, ctx):
        try:
            await join_vc.join(ctx)
        except:
            await ctx.send("`The Bot's already in a voice chat`")

    @commands.command(aliases=["leave_vc", "leave"])
    async def leave_voice(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()

    @commands.command(pass_context=True)
    async def play(self, ctx, url: str):
        try:
            url = ctx.message.content.split()[1]
            await play_aud.play(ctx, self.bot, url)
            
        except Exception as e:
            print(e)
            await ctx.send("`Error`")
