
import discord
from discord.ext import commands

class greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Server join meeting message
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.system_channel is not None:
            await guild.system_channel.send("Hello! I am Martin's tester bot! \nType !helps for a list of commands :)")
            print("Server join message sent!")
            print("-------------------------")

    # member join/leave server messages
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(1385703009287274529)
        await channel.send("Welcome " + str(member) + " woohoo!")
        print(str(member) + " has joined the server!")
        print("-------------------------")

    @commands.Cog.listener()
    async def on_member_remove(self, memeber):
        channel = self.client.get_channel(1385703009287274529)
        await channel.send("Goodbye " + str(memeber))
        print(str(memeber) + " has left the server")
        print("-------------------------")

async def setup(client):
    await client.add_cog(greetings(client))