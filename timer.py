from discord.ext import commands,tasks
from os import getenv
import discord
import traceback
import ffmpeg
import asyncio

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
    print(error_msg)

@bot.command()
async def leave(ctx):
    if ctx.guild.voice_client is None:
        await ctx.channel.send("接続していません")
        return

    #VC切断
    await ctx.guild.voice_client.disconnect()

@bot.command()
async def set(ctx,alarm):
    if ctx.guild.voice_client is None:
        #VC接続
        await ctx.author.voice.channel.connect()
    #タイマーセット/アラーム
    hmlist = countdowntime(alarm)
    timer = hmlist[0] * 3600 + hmlist[1] * 60
    await ctx.channel.send(f'{ctx.author.mention} アラームを{timer}秒後にセットしました')
    await asyncio.sleep(timer)
    ctx.guild.voice_client.play(discord.FFmpegPCMAudio("shiningStar.mp3"))
    await ctx.channel.send(f'{ctx.author.mention} {timer}秒が経過しました')

def countdowntime(alarm):
    counter = 0
    counth = 0
    hour = False
    minute = False
    for i in alarm:
        if i == 'h':
            hour = True
            counth = counter
            alarmh = int(alarm[0:counth])
        elif i == 'm' and counth == 0:
            minute = True
            countm = counter
            alarmm = int(alarm[counth:countm])
        elif i == 'm' and counth != 0:
            minute = True
            countm = counter
            alarmm = int(alarm[counth+1:countm])
        counter = counter + 1
    if hour == True and minute == True:
        return alarmh,alarmm
    elif hour == True and minute == False:
        return alarmh,0
    elif hour == False and minute == True:
        return 0,alarmm
    else:
        return 0,0

#botの起動とDiscordサーバーへの接続
#botのトークン
token = getenv('Token')
bot.run(token)