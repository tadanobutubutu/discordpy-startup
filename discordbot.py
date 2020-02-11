@@ -1,21 +1,28 @@
from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/ping":
        await message.channel.send("pong!")

token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(pass_context=True)
async def ping2(msg):  # 処理時間を返す
    startt = time.time()
    await msg.send("計測中……!")
    await msg.send("pong！\n結果:**"+str(round(time.time()-startt, 3))+"**秒だ！")

    @client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/ssrlogin":
        await message.channel.send("..login")

bot.run(Njc2MzgxNjY0MTMzMjUxMDky.XkIwHg.MLTdcUAZMEeM3x-yyQLwkbEocLM)
client.run(Njc2MzgxNjY0MTMzMjUxMDky.XkIwHg.MLTdcUAZMEeM3x-yyQLwkbEocLM)
