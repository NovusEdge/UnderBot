import discord, json

async def help(ctx):
    with open("embeds/help.json", "r") as help_file:
        embedObj = discord.Embed.from_dict( json.load(help_file)["embed"] )

    await ctx.send("`UnderBot's Help Menu:`")
    await ctx.send(embed=embedObj)
