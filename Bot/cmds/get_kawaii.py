import requests, json, discord

async def kawaii(ctx):
    kawaiiGif = requests.get( "https://api.giphy.com/v1/gifs/random?api_key=LSN3t1vDsXlV40noyN06kEGlBopLsZNQ&tag=kawaii&rating=g" )
    kawaiiGif = kawaiiGif.json()["data"]["images"]["original"]["url"]

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
