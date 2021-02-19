import discord
import os
import requests

from keep_alive import keep_alive

client = discord.Client()

# Bot init
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('Minecraft'))
  print('Hello {0.user}'.format(client))

# Listen for messages sent with $ prefix
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Returns a dad joke when a user types $joke
    if message.content.startswith('$joke'):
        headers = {'Accept': 'application/json'}
        joke = requests.get('https://icanhazdadjoke.com/', headers=headers)
        await message.channel.send(joke.json()['joke'])
    
    # Returns a dad joke when a user types $joke
    if message.content.startswith('$help'): 
        await message.channel.send('''These are all the current commands:
$joke to get a joke
$dog to get a picture of a dog
$cat to get a picture of a cat
$roast to get insulted
$yomama to get a yo mama joke
$swiftquote to get a Taylor Swift quote
since this bot is still in alpha development expect more commands to be added in the future

raylife - A bot coded for by DeadlyRayyan and Janirudev ''')

    # Returns a Url to a picture of a dog on $dog
    if message.content.startswith('$dog'):
        headers = {'Accept': 'application/json'}
        dog = requests.get('https://api.thedogapi.com/v1/images/search', headers=headers)
        await message.channel.send(dog.json()[0]['url'])

    # Returns a Url to a picture of a dog on $dog
    if message.content.startswith('$swiftquote'):
        headers = {'Accept': 'application/json'}
        swift = requests.get('https://api.taylor.rest/', headers=headers)
        await message.channel.send(swift.json()['quote'])

    # Returns a Url to a picture of a cat on $cat
    if message.content.startswith('$cat'):
        headers = {'Accept': 'application/json'}
        cat = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
        await message.channel.send(cat.json()[0]['url'])
    
    # Returns a yo mamma joke
    if message.content.startswith('$yomama'):
        headers = {'Accept': 'application/json'}
        yomomma = requests.get('http://api.yomomma.info', headers=headers)
        await message.channel.send(yomomma.json()['joke'])
    
    # Returns an insult
    if message.content.startswith('$roast'):
        headers = {'Accept': 'application/json'}
        roast = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json', headers=headers)
        await message.channel.send(roast.json()['insult'])
    
    # Returns a Url to a picture from Nasa on $space
    if message.content.startswith('$space'):
        headers = {'Accept': 'application/json'}
        space = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', headers=headers)
        await message.channel.send(f'{space.json()["hdurl"]}')

    # Returns a uncertainty when user inputs original, min, max values
    if message.content.startswith('$max'):

        orig = message.content[32:37]
        min = message.content[19:24]
        max = message.content[7:12]

        uncertainty = ((float(max) - float(min)) / 2) / float(orig)
        percentage_uncertainty = round(uncertainty * 100, 3)

        await message.channel.send(
            f'@{message.author},  your uncertainty is {uncertainty} and percentage uncertainty: {percentage_uncertainty}%'
        )

keep_alive()
client.run(os.getenv('TOKEN'))