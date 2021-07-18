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
    
@bot.command(passcontext=True, help = ':Let Me leave the Voice channel')
async def leave(ctx):
    await ctx.voice_client.disconnect()
    print('leave voice chat',ctx.author.voice.channel)

@bot.event
async def on_message(message) :
    # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
    await bot.process_commands(message) 
    if str(message.content).lower().startswith("hello"):
        await message.channel.send('Hi!')
    
    if str(message.content).lower().startswith("paimon"):
        await message.channel.send('ว่าจะได๋?')
    
    if str(message.content).startswith("หิวข้าว"):
        await message.channel.send('จะกินอาหารฉุกเฉินไหมล่ะห้ะ')
    
    if str(message.content).lower() in ['fuck','kuy']:
        await message.channel.purge(limit=1)


bot.run(myToken.get())