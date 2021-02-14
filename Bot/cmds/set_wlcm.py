import discord, json

async def set_welcome_channel(ctx, botObj, wlcm_chan, inst):
    with open("../.configs/welcome_config.json", "r") as f:
        data = json.load(f)

    with open("../.configs/welcome_config.json", "w") as f:
        ok = True

        for guild in data["guilds"]:
            if guild["guild_name"] == ctx.guild.name:
                guild["welcome_channel"] = ctx.channel.id
                guild["channel_name"] = ctx.channel.name
                ok = False
                inst.welcome_channel = ctx.channel.id
        if ok:
            data["guilds"].append({
                "welcome_channel": ctx.channel.id,
                "channel_name": ctx.channel.name,
                "guild_name": ctx.guild.name
            })

        json.dump(data, f)

    await ctx.send("This channel is now set as @UnderBot 's welcome channel")
