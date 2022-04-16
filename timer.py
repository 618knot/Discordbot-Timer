import discord

#botのトークン
Token = 'OTU1MTEwMDU3NjgxNDg1ODI1.Yjc5jg.OITf13hJftfBTT8Ttft1pFCdtoc'

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
client.run(Token)