from discord.ext import commands
from os import getenv
import discord

bot = commands.Bot(command_prefix='$')

#起動時の処理
@bot.event
async def on_ready():
    print("on_ready")
    print(bot.user.name) #bot name
    print(bot.user.id) #ID
    print(discord.__version__) #discord.pyのversion
    print("--------")
    await bot.change_presence(activity=discord.Game(name = "under development"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await message.channel.send(message)

    await bot.process_commands(message)

#コマンドごとの処理
@bot.command()
async def test(ctx, a):
    await ctx.send(a)

#botの起動とDiscordサーバーへの接続
#botのトークン
token = getenv('Token')
bot.run(token)