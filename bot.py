#!/usr/bin/env python3

# https://discord.com/api/oauth2/authorize?client_id=864995480919081031&permissions=3221343312&scope=bot

from os import getenv
from dotenv import load_dotenv
import discord
from collections import Counter

load_dotenv()
TOKEN = getenv("TOKEN")
GUILD_ID = 817460102495338536
CHANNEL_ID = 835667584288423956

class ShrekBot(discord.Client):
    frases = []

    async def carregar_frases(self):
        for guild in self.guilds:
            if guild.id == GUILD_ID:
                for text_channels in guild.text_channels:
                    if text_channels.id == CHANNEL_ID:
                        async for frase in text_channels.history(limit=None):
                            self.frases.append(frase)

    async def on_ready(self):
        await self.carregar_frases()

    async def on_message(self, message):
        if message.channel.id == CHANNEL_ID:
            self.frases.append(message)
        else:
            if message.guild.id == GUILD_ID and message.content == 'manda':
                mentions = []
                for frase in self.frases:
                    for mention in frase.mentions:
                        mentions.append(mention.name)
                leaderboard = ""
                for name, num in Counter(mentions).most_common():
                    leaderboard += f'{name}: {num}\n'
                await message.channel.send(leaderboard)

bot = ShrekBot()
bot.run(TOKEN)
