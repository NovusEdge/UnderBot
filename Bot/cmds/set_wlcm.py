import discord, json

async def set_welcome_channel(ctx, botObj, wlcm_chan):
    with open("../.configs/welcome_config.json", "w+") as f:
        data = json.load(f)

        for guild in data["guilds"]:
            if guild["guild_name"] == ctx.guild.name:
                guild = guild["welcome_channel"] = ctx.channel.id
                guild = guild["channel_name"] = ctx.channel.name

        json.dump(data, f)

    await ctx.send("This channel is now set as @UnderBot 's welcome channel")
