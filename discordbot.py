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

client.run(token)
