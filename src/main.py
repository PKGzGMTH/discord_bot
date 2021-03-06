import discord, random, json
from discord.ext import commands

f = open('data.json')
data = json.load(f)
f.close

genshin_chr = data["genshin_chr"].split(',')

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-'*80)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')

@bot.command()
async def what_time_is_it(ctx):
    """Just Ask Question."""
    await ctx.send(f'it\'s high noon')

@bot.command()
async def genshinroll(ctx):
    """pull some charecter in Genshin Impact."""
    char = genshin_chr[random.randint(0,22)]
    usr = str(ctx.message.author).split('#')[0]
    await ctx.send(f'{usr} got {char}')

@bot.command(pass_context = True) #passing context
async def salute(ctx): #context gets passed into the first parameter
    print(str(ctx.message.author))
    print(str(ctx.message.channel))
    print(str(ctx.message.content))

@bot.group()
async def cool(ctx):
    """Says if a user is cool."""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(data["TOKEN"])