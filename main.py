import os
import sys
import discord
from discord.ext import commands

#Client definition
client = discord.Client()

#User definition
user = discord.utils.get(client.users, name="USERNAME", discriminator="1234")
if user is None:
    print("User not found")

bot = commands.Bot(command_prefix = '/', intents=discord.Intents.all())


def load_cogs():
    """
    Pulls every .py file in the /cogs folder, and treats it like a cog.
    only cogs should be in the /cogs folder. 
    """

    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            bot.load_extension("cogs." + f[:-3])

def load_key_and_run():
    """
    Loads the first argument passed after 'python3 main.py',
    and treats it as a bot token.
    this allows you to run the bot by using:

    python3 main.py tokenGoesHere
    """

    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        bot.run(TOKEN)
    else:
        print('ERROR:\nYou must include a Discord bot token.\n- For more info, go to: https://discord.com/developers')

if __name__ == "__main__":
    load_cogs()
    load_key_and_run()


