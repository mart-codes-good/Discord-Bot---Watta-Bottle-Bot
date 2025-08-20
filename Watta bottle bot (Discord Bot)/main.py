# @author: Martin Tejada
# @version: 1.0
# @since: August 19th, 2025

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Managing discord permissions
intents = discord.Intents.all()

# Prefix before using discord commands, to call bot
client = commands.Bot(command_prefix='!', intents=intents)

# Message to let developer know that the bot is operational
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Yanxi Palace", url="https://www.youtube.com/watch?v=uCLoJTZ8YXg")) # this is an optional line of code
    print("Watta Bottle Bot is online and ready for use!")
    print("---------------------------")


# To be able to access the .py files in a diffrent folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

# To print to terminal to see what cogs were found
print(initial_extensions)

async def load_cogs():
    for extension in initial_extensions:
        await client.load_extension(extension)

# import each cog and load into bot
if __name__ == '__main__':
    import asyncio
    asyncio.run(load_cogs())

    # Retrive Discord bot API key from .env file
    BOT_KEY = os.getenv("watta_bot_key")
    client.run(BOT_KEY)
