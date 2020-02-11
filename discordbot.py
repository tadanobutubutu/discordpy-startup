import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/ping":
        await message.channel.send("pong!")

token = os.environ['DISCORD_BOT_TOKEN']

client.run(token)
