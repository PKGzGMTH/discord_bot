import discord, myToken
from discord.ext import commands

client = discord.Client()
#bot = commands.Bot(command_prefix= '>')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('paimon'):
        await message.channel.send('Yare Yare Daze')

client.run(myToken.get())

#bot.run(botTOKEN)