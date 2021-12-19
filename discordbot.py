from discord.ext import commands
from os import getenv
import traceback
import discord

token = getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='/')
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

client = discord.Client()
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        botRoom = client.get_channel(830452083680739339)
        announceChannelIds = [810832786659213316]
    if before.channel is not None and before.channel.id in announceChannelIds:
        await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
    if after.channel is not None and after.channel.id in announceChannelIds:
        await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")
client.run(token)
