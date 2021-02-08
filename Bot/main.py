import bot

if __name__ == "__main__":
    import discord, json, base64, os, pathlib

    path = pathlib.Path(__file__).parent.absolute()
    os.chdir(path)

    with open("../.configs/token_config", "r") as f:
        TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')

    b = bot.Bot(token=TOKEN, command_prefix="gb.")
    b.setup()
    b.run()
