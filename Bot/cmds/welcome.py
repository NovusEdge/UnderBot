import discord, json, time

async def get_roles(member):
    roles = member.guild.roles
    pass

async def welcome(member, botObj):

    with open("embeds/welcome.json", "r") as invite_file:
        embedObj = discord.Embed.from_dict( json.load(invite_file)["embed"] )

    await member.send("https://media.giphy.com/media/JuyhnRiWcPlAumeXnD/giphy.gif")
    await member.send(embed=embedObj)
    time.sleep(2.5)
    await member.send("Also, dont forget to introduce yourself in `#introduce-yourself`. :smiley:")


def get_chan(ctx):
    with open("../.configs/welcome_config.json", "r") as f:
        data = json.load(f)
        for guild in data["guilds"]:
            if guild["guild_name"] == ctx.guild.name:
                return guild


async def welcome_command(member, botObj):
    chan = get_chan(member)["welcome_channel"]

    # embedObj = discord.Embed.from_dict({
    #     "embed": {
    #         "title": f"Hello There {member.display_name}, Welcome to {member.guild.name}",
    #         "color": 9118641,
    #         "footer": {
    #             "text": "by UnderBot"
    #         },
    #         "thumbnail": {
    #             "url": "https://media.giphy.com/media/LtRidSX6NNG5HD0dnB/giphy.gif"
    #         },
    #         "author": {
    #             "name": "UnderBot",
    #             "icon_url": "https://raw.githubusercontent.com/NovusEdge/UnderBot/master/logo/logo.ico"
    #         },
    #         "fields": [ ]
    #     }
    # }["embed"])

    # await botObj.get_channel(chan).send(f"Hello There {member.mention}, Welcome to {member.guild.name}", embed=embedObj)

    await botObj.get_channel(chan).send(f"Hello There {member.mention}, Welcome to {member.guild.name}")
