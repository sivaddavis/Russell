import random
import requests
import secrets
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

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

@client.command(name='hello',
	description="Say hello to Russell!",
	brief="Greet Russell, the Wilderness Explorer",
	aliases=['hi', 'yo', 'sup'],
	pass_context=True)
async def hi(context):
        await client.say("Hello " + context.message.author.mention + ", how can I assist you today?")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('How can I assist?')
    print('------')

client.run(secrets.TOKEN)
