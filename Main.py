import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="%")

token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game('Your favorite singing neko'))
    print(f'Welcome to Radiokayu!')

@client.command()
async def hello(ctx) :
    await ctx.send(f'Hello!')
    
client.run(token)