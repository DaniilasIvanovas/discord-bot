import responses, discord, configparser, os, random


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

photos = []


async def send_photo(channel):
    await channel.send(file=discord.File('./pictures/' + photos[random.randint(0, len(photos))]))
    # with open('my_image.png', 'rb') as f:
    #     picture = discord.File(f)
    #     await channel.send(file=picture)


def run_discord_bot():
    conf = configparser.ConfigParser()
    conf.read('token.ini')
    TOKEN = conf['info']['TOKEN']

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        channel = client.get_channel(1038548451446763622)
        # await channel.send('Labas visiems! Tomas grizo')
        # await channel.send(file=discord.File('./pictures/zenius.png'))
        for f in os.listdir('./pictures'):
            photos.append(f)

    @client.event
    async def on_message(message):
        # Make sure pictures doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        channel_obj = message.channel
        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        # if user_message[0] == '?':
        #     user_message = user_message[1:]  # [1:] Removes the '?'
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)

        if user_message == "imesk foto" or user_message == 'imesk fotke':
            await send_photo(channel_obj)

    client.run(TOKEN)

