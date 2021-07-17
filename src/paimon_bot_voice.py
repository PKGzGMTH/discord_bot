import discord, myToken
from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix= '>')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(passcontext=True, help = ':Let Me join the Voice channel')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    print('\njoining voice chat ',ctx.author.voice.channel)
    print(f'cmd : {bot}')
    
@bot.command(passcontext=True, help = ':Let Me leave the Voice channel')
async def leave(ctx):
    await ctx.voice_client.disconnect()
    print('leave voice chat',ctx.author.voice.channel)
    print(f'cmd : {bot}')

bot.run(myToken.get())