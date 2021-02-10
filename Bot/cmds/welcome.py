import discord, json, time

async def welcome(member, botObj):

    with open("embeds/welcome.json", "r") as invite_file:
        embedObj = discord.Embed.from_dict( json.load(invite_file)["embed"] )

    await member.send(embed=embedObj)
    time.sleep(1.5)
    await member.send("Also, dont forget to introduce yourself in `#introduce-yourself`. :smiley:")


async def welcome_command(ctx):

    with open("embeds/welcome.json", "r") as invite_file:
        embedObj = discord.Embed.from_dict( json.load(invite_file)["embed"] )

    await ctx.send(embed=embedObj)
    time.sleep(1.5)
    await ctx.send("Also, dont forget to introduce yourself in `#introduce-yourself`. :smiley:")
