import discord, json, re

async def setprefix(ctx, botObj, prefix):
    try:
        botObj.command_prefix = prefix
        await ctx.send(f"`Command Prefix` changed to `{prefix}`")

    except Exception as e:
        print(e)
        await ctx.send(r"`Error in changing Command Prefix :(`")
