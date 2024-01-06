
import discord
from discord.ext import commands

from logger import logger

from config import DISCORD_AUTH_TOKEN
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def countdown(ctx, arg):
    datetime_str = arg
    datetime_obj = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')
    formatted_datetime = datetime_obj.strftime("%Y%m%dT%H%M%S")
    await ctx.send(f"https://www.timeanddate.com/countdown/generic?iso={formatted_datetime}&p0=60&font=cursive")

#https://www.timeanddate.com/countdown/generic?iso=2024 01 12 T 14 30 40&p0=60&font=cursive
bot.run(DISCORD_AUTH_TOKEN, log_handler=None)
