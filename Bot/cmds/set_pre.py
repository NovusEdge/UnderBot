import discord, json, re

async def setprefix(ctx, botObj):
    try:
        pre = get_prefix(ctx)
        botObj.command_prefix = pre

        ctx.send(f"`Command Prefix` changed to `{pre}`")
    except:
        ctx.send(r"`Error in changing Command Prefix :(`")

def get_prefix(ctx):
    msg = ctx.message.content
    matches = re.findall(r'''(["'])(?:(?=(\\?))\2.)*?\1''', msg)

    return matches[0]
