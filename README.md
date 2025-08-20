# Watta Bottle Bot (Discord Bot)

A Discord bot made in Python using discord.py with cogs architecture (each cog is a Python class that subclasses commands).
This project is mainly for learning, bot development, trying out new tools, and practicing more advanced features over time.
Currently, it comes with moderation commands and some AI-powered engagement tools.

Note:
The prefix of the bot is set to '!'. 
- e.g. for joke command: !joke
  
The word filter is currently set to "poop", but it can be expanded to loop through a custom list of words you want filtered out.

## Features
- Moderation Tools (!kick, !ban)
- Basic Word Filtering (deletes certain words)
- Fun AI Commands (generated jokes, riddles, thinking puzzles, etc!)
- Event Commands (Server join/leave messages, Bot join messages)

## Dependencies
- discord.py
- openai
- python-dotenv

## Future plans
* Data Tools (in development)
  * !csv, !graph, !table, !scatterplot (future data visualization commands)
  * Refining prompts to be less verbose, with possible soft tweaks to logic (hopefully won't cause issues)
* Bot port to Nextcord.py
