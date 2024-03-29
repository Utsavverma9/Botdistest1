# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('ya! We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$UVhello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$UVUTSAV'):
      await message.channel.send('What do you want to know about UTSAV?')
    elif message.content.startswith('$UVhelp'):
      await message.channel.send('ok so you want help from the bot')


try:
  
  token = "MTIxODEzMjk0MDMwMzc2NTU2NQ.GtwtJq.yGEM22Hfib4gm1SroABctl7n5SRzifw2bNvbe4" 
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
