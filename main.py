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





bot.run('MTIyMzIwNTU3NDQ4NTg3MjczMA.GC77Ws.12lsFsVij2MV7gpQ-2-UE1rLrxTtyvHbcmAtMU') 


