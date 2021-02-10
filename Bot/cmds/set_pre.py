import discord, json, re

async def setprefix(ctx, botObj):
    try:
        pre = get_prefix(ctx)
        print(pre)
        botObj.command_prefix = pre

        await ctx.send(f"`Command Prefix` changed to `{pre}`")
    except:
        await ctx.send(r"`Error in changing Command Prefix :(`")

def get_prefix(ctx):
    msg = ctx.message.content
    return msg.partition("prefix=")[2][1:-1]
