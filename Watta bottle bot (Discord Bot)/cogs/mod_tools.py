import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from dotenv import load_dotenv
import os

class mod_tools(commands.Cog):

    def __init__(self, client):
        self.client = client

    # kick command
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"User {member} has been kicked")

        print(f"{member} was kicked")
        print("---------------------") 

    # if missing permission to kick
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Missing permissions to kick user")

    # ban command
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"User {member} has been banned")

        print(f"{member} was banned")
        print("---------------------")

    # if missing permissiosn to ban
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Missing permissions to kick user")

    # Disconnect from voicecall
    @commands.command()
    async def dc(self, ctx):
        pass

    # Help command that outlines all testable commands
    @commands.command()
    async def info(self, ctx):
        await ctx.send("""The current commands available are:
                        !anagrams        
                        !ban             
                        !csv           (in development)  
                        !dc            (in development)  
                        !funfact
                        !graph         (in development)  
                        !help          (built-in)  
                        !info          (this command)  
                        !joke  
                        !kick           
                        !pun  
                        !puzzle         
                        !riddle  
                        !scatterplot   (in development)  
                        !table         (in development)  
                        !twister  
                    
                Automated Functions:

                Bot Status Alerts (dev console only)

                Bot On Server Join Message

                Member Join/Leave Logs

                Message Filters (ex: swear words)

                    """)


    # Detecting certain words from discord text channels
    @commands.Cog.listener()
    async def on_message(self, message):
        
        # if word in brackets is detected, delete message and dm user
        # for multiple words, create a list and have it cycle through list to check and find word
        if "poop" in message.content.lower():
            await message.delete()
            await message.channel.send("Don't say that word!")

async def setup(client):
    await client.add_cog(mod_tools(client))