from discord.ext import commands
from os import getenv
import discord


#接続に必要なオブジェクト
client = discord.Client()

#起動時の処理
@client.event
async def on_ready():
    print("on_ready")
    print(client.user.name) #bot name
    print(client.user.id) #ID
    print(discord.__version__) #discord.pyのversion
    print("--------")
    await client.change_presence(activity=discord.Game(name = "under development"))

#botの起動とDiscordサーバーへの接続
#botのトークン
token = getenv('Token')
client.run(token)