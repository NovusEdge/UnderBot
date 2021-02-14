import discord, json

async def help(ctx):
    if ctx.message.content == "ub.help":
        await help_main(ctx)
        return

    spec = ctx.message.content.split()[1]

    if spec == "":
        await help_main(ctx)

    elif spec == "kawaii":
        await help_kawaii(ctx)

    elif spec == "voice":
        await help_vc(ctx)

    elif spec == "misc":
        await help_misc(ctx)

    elif spec == "config":
        await help_config(ctx)

    else:
        await help_main(ctx)

async def help_main(ctx):
    with open("embeds/help_main.json", "r") as help_file:
        embedObj = discord.Embed.from_dict( json.load(help_file)["embed"] )

    await ctx.send("`UnderBot's Help Menu:`")
    await ctx.send(embed=embedObj)

async def help_kawaii(ctx):
    with open("embeds/help_kawaii.json", "r") as help_file:
        embedObj = discord.Embed.from_dict( json.load(help_file)["embed"] )

    await ctx.send("`Kawaii support`")
    await ctx.send(embed=embedObj)

async def help_vc(ctx):
    with open("embeds/help_vc.json", "r") as help_file:
        embedObj = discord.Embed.from_dict( json.load(help_file)["embed"] )

    await ctx.send("`Voice support`")
    await ctx.send(embed=embedObj)

async def help_misc(ctx):
    with open("embeds/help_misc.json", "r") as help_file:
        embedObj = discord.Embed.from_dict( json.load(help_file)["embed"] )

    await ctx.send("`UnderBot's Misc. Help Menu:`")
    await ctx.send(embed=embedObj)

async def help_config(ctx):
    with open("embeds/help_bot_config.json", "r") as help_file:
        embedObj = discord.Embed.from_dict( json.load(help_file)["embed"] )

    await ctx.send("`Commands for bot-config`")
    await ctx.send(embed=embedObj)
