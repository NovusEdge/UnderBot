from cmds.voice import join_vc, play_aud, add_url, playlist_play
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
        if voice.is_playing():
            await self.stop(ctx)

        if voice and voice.is_connected():
            await voice.disconnect()

    @commands.command(pass_context=True)
    async def play_url(self, ctx, url: str):
        try:
            url = ctx.message.content.split()[1]
            await play_aud.play(ctx, self.bot, url)

        except Exception as e:
            print(e)
            await ctx.send("`Error`")

    @commands.command()
    async def stop(self, ctx):
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client.is_playing:
            voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything right now.")

    @commands.command()
    async def pause(self, ctx):
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client.is_playing:
            voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything right now.")

    @commands.command()
    async def resume(self, ctx):
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client.is_playing:
            voice_client.resume()
        else:
            await ctx.send("The bot is already playing right now.")

    @commands.command(aliases=["add_url"], pass_context=True)
    async def add(self, ctx, url: str):
        await add_url.add(url)

    @commands.command(aliases=["pplay", "playplst"])
    async def play_playlist(self, ctx):
        await playlist_play.play(ctx, self.bot)
