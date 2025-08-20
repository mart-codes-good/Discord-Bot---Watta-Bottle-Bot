import pandas as pd
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from Ai_Agent import get_llm_response

topics = ["math", "choose the strangest topic ever!", "science", "forests", "echos", "school", "food", "choose a unique topic please :)", "dinosaurs", "space", "choose the randomest topic you can think of!", "not scarecrows"]

class fun_messages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.counter = 0

    # Requests joke from OpenAi key
    @commands.command()
    async def joke(self, ctx):

        await ctx.send(get_llm_response("DO NOT MAKE A PLAY ON WORDS, but tell me something funny. Please give a set up and a punchline"))
        self.counter += 1
        print("Joke sent!")
        print("-------------------------")

        if self.counter > len(topics):
            self.counter = 0
            

    # Requests a riddle from OpenAi key, and marks the answer as a spoiler
    @commands.command()
    async def riddle(self, ctx):
        riddle = get_llm_response("Tell me a riddle about " + topics[self.counter] + "! but put || || around the answer :)")
        await ctx.send(riddle)
        self.counter += 1

        print("Riddle sent!")
        print("-------------------------")

        if self.counter > len(topics):
            self.counter = 0

    # Request an pun/joke from open Ai
    @commands.command()
    async def pun(self, ctx):
        pun = get_llm_response("Tell me a pun :) ! based of " + topics[self.counter])
        await ctx.send(pun)
        self.counter += 1

        print("Pun sent!")
        print("---------------------")

        if self.counter > len(topics):
            self.counter = 0

    # Request a fun fact from open Ai, prompt says obscure to try to make it more interesting
    @commands.command()
    async def funfact(self,ctx):
        funfact = get_llm_response("Give me an obscure fun fact, feel free to include any findings such as statistics")
        await ctx.send(funfact)
        print("Fun fact sent!")
        print("---------------------")

    # Requests an anagram from open Ai and has user guess the anagram. marks answer as spoiler
    @commands.command()
    async def anagram(self, ctx):
        anagram = get_llm_response("Choose a unique word and then an anagram based of that word. then ask me to guess the anagram of the word you chose. and then put the annagram with || || around it")
        await ctx.send(anagram)

        print("Anagram sent!")
        print("--------------")
        
        if self.counter > len(topics):
            self.counter = 0
    
    # Requests a short tongue twister from open Ai
    @commands.command()
    async def twister(self, ctx):
        twister = get_llm_response("Make a tongue twister for me based of " + topics[self.counter])
        await ctx.send(twister)

        print("Tongue twister sent!")
        print("--------------")
        
        if self.counter > len(topics):
            self.counter = 0

    # Requests a lateral thinking problem (puzzle) from open Ai, marks answer as spoiler
    @commands.command()
    async def puzzle(self, ctx):
        puzzle = get_llm_response("Give me a thinking problem! please put || || around the answer :)")
        await ctx.send(puzzle)

        print("Thinking puzzle sent!")
        print("--------------")

        if self.counter > len(topics):
                self.counter = 0

async def setup(client):
    await client.add_cog(fun_messages(client))