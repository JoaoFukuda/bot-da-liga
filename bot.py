#!/usr/bin/env python3

# https://discord.com/api/oauth2/authorize?client_id=864995480919081031&permissions=3221343312&scope=bot

from os import getenv
from dotenv import load_dotenv
import discord
from collections import Counter

load_dotenv()
TOKEN = getenv("TOKEN")
GUILD = "Sistemas de Informação - EACH-USP"

frases = []

class ShrekBot(discord.Client):
    async def on_ready(self):
        print(f'Connected to discord as {bot.user}')
        for guild in self.guilds:
            if guild.id == 817460102495338536:
                for tc in guild.text_channels:
                    if tc.id == 835667584288423956:
                        async for message in tc.history(limit=None):
                            frases.append(message)

    async def on_message(self, message):
        if message.channel.id == 835667584288423956:
            frases.append(message)
        else:
            if message.guild.id == 817460102495338536 and message.content == 'manda':
                mentions = []
                for frase in frases:
                    for mention in frase.mentions:
                        mentions.append(mention.name)
                message_to_send = ""
                for name, num in Counter(mentions).most_common():
                    message_to_send += f'{name}: {num}\n'
                await message.channel.send(message_to_send)

bot = ShrekBot()
bot.run(TOKEN)
