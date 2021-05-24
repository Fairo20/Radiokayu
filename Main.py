import discord
import logging
import json
import os
from discord.ext import commands


token = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix="%")

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game('Your favorite singing neko'))
    print('Welcome to Radiokayu!')

#@client.event
#async def on_message(message):
#   if message.author == client.user:
#        return

#    if message.content.startswith('%hello'):
#        await message.channel.send('Hello!')

@client.command()
async def hello(ctx) :
    await ctx.send(f'Hello!')
    
client.run(token)