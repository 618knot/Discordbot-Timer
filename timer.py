from discord.ext import commands
from os import getenv
import discord
import traceback
import ffmpeg

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print("on_ready")
    print(bot.user.name) #bot name
    print(bot.user.id) #ID
    print(discord.__version__) #discord.pyのversion
    print("--------")
    await bot.change_presence(activity=discord.Game(name = "under development"))


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx,arg):
    await ctx.send(arg)

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("あなたはボイスチャンネルに接続していません")
    
    #VC接続
    await ctx.author.voice.channel.connect()

@bot.command()
async def leave(ctx):
    if ctx.guild.voice_client is None:
        await ctx.channel.send("接続していません")
        return

    #VC切断
    await ctx.guild.voice_client.disconnect()

@bot.command()
async def play(ctx):
    if ctx.guild.voice_client is None:
        await ctx.channel.send("接続していません。")
        return
    ctx.guild.voice_client.play(discord.FFmpegPCMAudio("shiningStar.mp3"))

#botの起動とDiscordサーバーへの接続
#botのトークン
token = getenv('Token')
bot.run(token)