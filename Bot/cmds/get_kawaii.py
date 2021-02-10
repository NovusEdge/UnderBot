import requests, json, discord, time

async def kawaii(ctx):
    loadingGif = "https://media1.tenor.com/images/fd07a59a62cc79a98487ac9196a6a29b/tenor.gif?itemid=12547924"

    emObj = discord.Embed.from_dict({
    "embed": {
        "title": "Generating Cuteness...",
        "image": {
            "url": f"{loadingGif}"
        },
        "color": 1035781,
        "footer": {
            "text": "by UnderBot"
        },
        "author": {
            "name": "UnderBot",
            "icon_url": "https://raw.githubusercontent.com/NovusEdge/UnderBot/master/logo/logo(pexels-sebastiaan-stam-1097456).ico"
        },
        "fields": [ ]
    }
    }["embed"])

    waitmsg = await ctx.send(embed=emObj)

    try:
        kawaiiGif = requests.get( "https://api.giphy.com/v1/gifs/random?api_key=LSN3t1vDsXlV40noyN06kEGlBopLsZNQ&tag=kawaii&rating=g" )
        kawaiiGif = kawaiiGif.json()["data"]["images"]["original"]["url"]

        time.sleep(2)
        await waitmsg.delete()

        embedObj = discord.Embed.from_dict({
          "content": "Dog: ",
            "embed": {
                "color": 40447,
                "footer": {
                    "text": "Gif by: https://giphy.com"
                    },
                "image": {
                    "url": f"{ kawaiiGif }"
                    },
                "author": {
                    "name": "UnderBot",
                    "url": "https://discordapp.com",
                    "icon_url": "https://raw.githubusercontent.com/NovusEdge/UnderBot/master/logo/logo.ico"
                },
        "fields": [ ]
        }
        }['embed'])
        await ctx.send(embed=embedObj)

    except:
        time.sleep(2)
        await waitmsg.delete()
        await ctx.send("`Error generating cuteness :cry:`")
