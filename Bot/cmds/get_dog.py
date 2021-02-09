import requests, json, discord

async def dogs(ctx):
    dogPic = requests.get( 'https://dog.ceo/api/breeds/image/random' ).json()['message']

    embedObj = discord.Embed.from_dict({
          "content": "Dog: ",
            "embed": {
                "title": "Here's a cute dog, Enjoy :hugging:",
                "color": 40447,
                "footer": {
                    "text": "Image by: https://dog.ceo/dog-api/"
                    },
                "image": {
                    "url": f"{ dogPic }"
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
