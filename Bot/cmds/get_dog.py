import requests, json, discord, time

async def dogs(ctx):
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
    time.sleep(2)
    await waitmsg.delete()

    try:
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
    except:
        time.sleep(2)
        await waitmsg.delete()
        await ctx.send("`Error generating cuteness :cry:`")
