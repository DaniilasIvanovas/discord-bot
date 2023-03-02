import discord, configparser, os, random
import words as w # Tomo trigger zodziai
import json, datetime
from addons import wiki
from discord.ext import commands

conf = configparser.ConfigParser()
conf.read('token.ini')
TOKEN = conf['info']['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
guild_id = int(conf['info']['guild_id'])
client = discord.Client(intents=intents)
guild = client.get_guild(guild_id)


@bot.event
async def on_ready():
    print('Tomas is now running...')


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
async def keiksmai(msg):
    message = msg.author.mention + ' keiktis negalima!'
    with open('keiksmai.txt', 'r') as file:
        for line in file.readlines():
            words = line.rstrip().split(',')

    for word in words:
        if word in msg.content.split(' '):
            await msg.channel.send(message)
            with open('data.json', 'r') as f:
                data = json.loads(f.read())
            with open('data.json', 'w') as f:
                if str(msg.author.id) in data:
                    if data[str(msg.author.id)] == 3:
                        await msg.channel.send("Nu vsio tau")
                        member = guild.get_member(msg.author.id)
                        await member.timeout(datetime.timedelta(seconds=30))
                        data[str(msg.author.id)] = 0
                        json.dump(data, f)
                    else:
                        data[str(msg.author.id)] += 1
                        json.dump(data, f)
                else:
                    data.update({str(msg.author.id): 1})
                    json.dump(data, f)


@bot.listen('on_message')
async def kreipimasis(msg):
    msg_c = str(msg.content).lower()
    if any(x in msg_c for x in w.vardai):
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
                    await msg.channel.send('Tai atrasyk...')
        except TimeoutError:
            await msg.channel.send('Nu tai kas yra?')


@bot.command(name='ateik', pass_context=True)
async def ateik(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command(name='iseik', pass_context=True)
async def iseik(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()


@bot.command(name='wiki')
async def search(ctx, arg):
    try:
        answer = wiki.get_answer(arg)
        if isinstance(answer, list):
            text = answer[0]
            link = answer[1]
            await ctx.send(text + '\n' + '\n' + 'Read more at: ' + link)
        else:
            await ctx.send(answer)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send('Missing argument...')


def run_bot():
    bot.run(TOKEN)
