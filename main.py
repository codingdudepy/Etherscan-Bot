#Importing required modules
import discord
import requests
from discord.ext import tasks
import json
from discord.ext import commands

#intializing discord bot and setting prefix
client = commands.Bot(command_prefix='!')



@client.command()
async def totalsupply(ctx):
    response = requests.get("https://api.etherscan.io/api?module=stats&action=ethsupply&apikey=xxxxxxxxxxxxxxxxxx")
    data = response.json()
    parsing_data = data['result']
    embedVar = discord.Embed(title="Total supply of etheruem was: ", description=f"{parsing_data}", color=0x0000FF)
    await ctx.send(embed=embedVar)

@client.command()
async def amount(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Please insert a wallet address')
    title = await client.wait_for('message', check=check)
    response = requests.get(f"https://api.etherscan.io/api?module=account&action=balance&address={title.content}&tag=latest&apikeyxxxxxxxxxxxxxxxxxx")
    data = response.json()
    parsing_data = data['result']
    embedVar = discord.Embed(title="Amount of etheruem in this persons wallet is: ", description=f"{parsing_data}", color=0x0000FF)
    await ctx.send(embed=embedVar)

@client.command()
async def ethprice(ctx):
    response = requests.get("https://api.etherscan.io/api?module=stats&action=ethprice&apikey=xxxxxxxxxxxxxxxxxx")
    data = response.json()
    parsing_data = data['result']['ethusd']
    embedVar = discord.Embed(title="Etheruems last price was: : ", description=f"${parsing_data}", color=0x0000FF)
    await ctx.send(embed=embedVar)

@client.command()
async def getgas(ctx):
    response = requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=xxxxxxxxxxxxxxxxxx")
    data = response.json()
    parsing_data = data['result']['FastGasPrice']
    embedVar = discord.Embed(title="Why is the Gas Price High Today?", description=f"***Gas Price: ***${parsing_data}", color=0x0000FF)
    embedVar.add_field(name="Gas Guzzlers", value="Almost", inline=False)
    await ctx.send(embed=embedVar)


client.run("discord token(can get at discord dev portal)")
