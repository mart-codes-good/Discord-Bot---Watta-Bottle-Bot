import pandas as pd
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class data_commands(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def csv(self, ctx):
        await ctx.send("Test")

    @commands.command()
    async def graph(self, ctx):
        await ctx.send("Test")

    @commands.command()
    async def table(self, ctx):
        await ctx.send("Test")

    @commands.command()
    async def scatterplot(self, ctx):
        await ctx.send("Test")
    
async def setup(client):
    await client.add_cog(data_commands(client))
     