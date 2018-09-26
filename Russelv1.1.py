import random
import requests
import config
import aiohttp
import json
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot 

BOT_PREFIX = ("?", "!")
CONSTANT = 1000000000000000000

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='1-10',
    description="Gives you a random number from 1-10",
    brief="Rate me",
    aliases=['rate_me', 'hot_or_not', 'on_a_scale'],
    pass_context=True)
async def onetoten(context):
    possible_responses = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="in the Wilderness"))
    print(client.user.name + "is online and ready to assist!")

@client.command(name='hello',
    description="Say Hello to Russell!",
    brief="Greet Russell, the Wilderness Explorer",
    aliases=['hi', 'yo', 'sup'],
    pass_context=True)
async def hi(context):
        await client.say("Hello " + context.message.author.mention + ", how can I assist you today?")

@client.command(name='crypto',
    description="Shows current prices for Bitcoin, Ethereum, Pascal and portfolio",
    brief="Check on current Portfolio status",
    aliases=['coins', 'bitcoin', 'ethereum', 'pascal'],
    pass_context=True)
async def crypto(context):
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['data']['amount'])
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Ethereum price is: $" + response['data']['amount'])
        url = 'https://poloniex.com/public?command=returnTicker'
        btcpasc = float(requests.get(url).json()['BTC_PASC']['last'])
        pascconvert = float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount']) * btcpasc
        pascal = str(round((pascconvert), 2))
        await client.say("Pascal price is: $" + pascal)
        btcsell_price = float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount'])
        btc_exchangeflat = float(0.02041137)
        btccurrent_valuationex = str(round((btcsell_price * btc_exchangeflat), 2))
        btcex = str(round((btc_exchangeflat), 4))
        await client.say("You currently have ~" + btcex + " BTC worth $" + btccurrent_valuationex + " in the exchange")
        url = "https://api.etherscan.io/api?module=account&action=balance&address=0xe84725720cb922151205cb66fcff9a4d54e85d5a&tag=latest"
        sell_price = float(requests.get('https://api.coinbase.com/v2/prices/ETH-USD/sell').json()['data']['amount'])
        eth_stash = int(requests.get(url).json()['result'])/CONSTANT
        current_valuation = str(round((sell_price * eth_stash), 2))
        ethwallet = str(round((eth_stash), 4))
        await client.say("You currently have ~" + ethwallet + " ETH worth $" + current_valuation + " in your wallet")
        eth_exchangeflat = float(1.4521)
        current_valuationex = str(round((sell_price * eth_exchangeflat), 2))
        ethex = str(eth_exchangeflat)
        await client.say("You currently have ~" + ethex + " ETH worth $" + current_valuationex + " in the exchange")
        pascalflat = float(50.9015)
        pascex = str(pascalflat)
        pascalex = str(round((pascconvert * pascalflat), 2))
        await client.say("You currently have ~" + pascalex + " PSC worth $" + pascalex + " in the exchange")
        portfolio_valuation = str(round((btcsell_price * btc_exchangeflat) + (sell_price * eth_stash) + (sell_price * eth_exchangeflat) + (pascconvert * pascalflat), 2))
        await client.say("Total, your portfolio is worth $" + portfolio_valuation)


client.run(config.TOKEN)
