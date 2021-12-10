# Making a Discord Bot!!
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@bot.command()
async def add(ctx, num1:float, num2:float):
    await ctx.reply(num1+num2)


bot.run(getenv('TOKEN'))