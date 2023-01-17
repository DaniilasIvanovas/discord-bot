import responses, discord, configparser, os, random
import words as w # Tomo trigger zodziai
from discord.ext import commands

conf = configparser.ConfigParser()
conf.read('token.ini')
TOKEN = conf['info']['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='fraze', help="Imesiu Plankio fraze is Ievos database")
async def frazes(ctx):
    await ctx.send(random.choice(w.frazes))


@bot.command(name='izeisk', help='Izeisiu')
async def izeidimas(ctx, arg):
    if arg == '<@285773249353351180>':
        await ctx.send('Meistro izeidinet negalima')
    elif arg =='<@1064896422975119430>':
        await ctx.send('ragana gaidys')
    else:
        await ctx.send(arg + ' tu esi blogas zmogus')


@bot.listen('on_message')
async def chat(msg):
    message = msg.author.mention + ' keiktis negalima!'
    with open('keiksmai.txt', 'r') as file:
        for line in file.readlines():
            words = line.rstrip().split(',')

    for word in words:
        if word in msg.content:
            await msg.channel.send(message)


@bot.listen('on_message')
async def sveikas(msg):
    if any(x in msg.content for x in w.sveikinimai) and any(x in msg.content for x in w.vardai):
        await msg.channel.send(random.choice(w.sveikinimai))


@bot.listen('on_message')
async def kreipimasis(msg):

    if any(x in msg.content for x in w.vardai):
        await msg.channel.send(random.choice(w.atsakas))
        response = await bot.wait_for('message', timeout=10, check=lambda m: m.author == msg.author)

        if response.content in ['imesk fotke', 'imesk foto', 'atsiusk fotke', 'atsiusk foto']:
            photos = []
            for f in os.listdir('./pictures'):
                photos.append(f)
            await msg.channel.send(file=discord.File('./pictures/' + random.choice(photos)))
            await msg.channel.send('Va prasau')
        try:
            if response.content in ['kaip sekasi?', 'kaip einasi?', 'kaip sekasi', 'kaip einasi']:
                await msg.channel.send(random.choice(['normaliai', 'blogai...', 'gerai haha', 'visai nieko', 'super',
                                                      'puse velnio']))
                await msg.channel.send('O tau kaip?')
                try:
                    response_kaip = await bot.wait_for('message', timeout=10, check=lambda m: m.author == msg.author)

                    if response_kaip.content in ['blogai', 'nekaip', 'Blogai', 'Nekaip']:
                        await msg.channel.send('Kaip gaila...')
                    elif response_kaip.content == 'normaliai':
                        await msg.channel.send('Supratau')
                    elif response_kaip.content == 'gerai':
                        await msg.channel.send('Dziugu girdet!')
                except TimeoutError:
                    await msg.channel.send('Tai atrasyk blet')
        except TimeoutError:
            await msg.channel.send('Tai atrasyk blet')


bot.run(TOKEN)
