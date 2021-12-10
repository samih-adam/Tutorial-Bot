# Making a Discord Bot!!
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import yfinance as yf
from yfinance.ticker import Ticker
import os
import requests
import json


load_dotenv()

appl = yf.Ticker("AAPL")

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@bot.command()
async def add(ctx, num1:float, num2:float):
    await ctx.reply(num1+num2)

@bot.command()
async def stock(ctx):
    
    apple = str(appl.info['dividendRate'])
    print(apple)
    await ctx.reply('Here is your dividend rate ' + apple)


bot.run(getenv('TOKEN'))