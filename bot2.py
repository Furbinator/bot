from discord.ext.commands import Bot
import random
import discord
import time
import urllib.request, json


BOT_PREFIX = "\\"
TOKEN = "NDMwNjE0MTE3NzU4NTMzNjMy.DaSwSQ.rPimEBXEiL_kNp3ZpTiLKdqnuWA"
server = discord.Server(id='370127079863484416')

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def hellno(skip = False):
    await client.say("The timer has begun...")
    while 1:
        if time.gmtime().tm_min == 0 or skip == True:
            west = list()
            for member in client.get_all_members():
                if member.bot == False:
                    west.append(member.id)
            await client.say('<@!' + random.choice(west) + '>')
            with urllib.request.urlopen("http://imgur.com/r/hentai/hot.json") as url:
                data = json.loads(url.read().decode())
                var1 = data['data'][random.randint(0, len(data['data']))]['hash']
                var2 = data['data'][random.randint(0, len(data['data']))]['ext']
            await client.say('https://imgur.com/' + var1 + var2)

@client.command()
async def hello():
    west = list()
    for member in client.get_all_members():
        if member.bot == False:
            west.append(member.id)
    await client.say('<@!' + random.choice(west) + '>')
    with urllib.request.urlopen("http://imgur.com/r/hentai/hot.json") as url:
        data = json.loads(url.read().decode())
        var1 = data['data'][random.randint(0, len(data['data']))]['hash']
        var2 = data['data'][random.randint(0, len(data['data']))]['ext']
    await client.say('https://imgur.com/' + var1 + var2)
client.run(TOKEN)
