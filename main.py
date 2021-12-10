# Making a Discord Bot!!
import discord
from discord import message
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import yfinance as yf
from yfinance.ticker import Ticker
import os
import requests
import json

client = discord.Client()

load_dotenv()

appl = yf.Ticker("AAPL")
msft = yf.Ticker("MSFT")
spy = yf.Ticker("SPY")

bot = commands.Bot(command_prefix='.')

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_message(message):
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)


@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@bot.command()
async def add(ctx, num1:float, num2:float):
    await ctx.reply(num1+num2)

@bot.command()
async def appl(ctx):
    
    apple = str(appl.info['dividendRate'])
    print(apple)
    await ctx.reply('Here is your dividend rate ' + apple)

@bot.command()
async def microsoft(ctx):
    
    microsoft = str(msft.info['dividendRate'])
    print(microsoft)
    microsoft_2 = msft.quarterly_balance_sheet
    print(microsoft_2)
    await ctx.reply('Here is your dividend rate ' + microsoft)
    




bot.run(getenv('TOKEN'))