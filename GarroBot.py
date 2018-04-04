# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import time
import random
import urllib.request, json
import asyncio

TOKEN = 'NDMwNjE0MTE3NzU4NTMzNjMy.DaSwSQ.rPimEBXEiL_kNp3ZpTiLKdqnuWA'

client = discord.Client()
server = discord.Server(id='370127079863484416')

def Boolczech(x):
    if x.lower() in ['true']:
        return True
    return False

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('\\hello'):
        array = message.content.split(' ')
        var = False
        if len(array) > 1: 
            var = Boolczech(array[1].lower())
        while 1:
            if time.gmtime().tm_min == 0 or var == True:
                west = list()
                for member in client.get_all_members():
                    if member.bot == False:
                        await client.send_message(message.channel,'<@!' + member.id + '>')
                        with urllib.request.urlopen("http://imgur.com/r/softwaregore/hot.json") as url:
                            data = json.loads(url.read().decode())
                            var1 = data['data'][random.randint(0, len(data['data'])-1)]['hash']
                            var2 = data['data'][random.randint(0, len(data['data'])-1)]['ext']
                        await client.send_message(message.channel,'https://imgur.com/' + var1 + var2)
                        if var == True:
                            var = False
                            continue
            await asyncio.sleep(60)

    if message.content.startswith('\\help'):
        await client.send_message(message.channel, '```\n\
\\hello - mentions someone at random and sends them a nsfw image every hour, on the hour. (or type \\hello True to send one immediately)\n\
\\help - displays this menu\n\
if you have any problems, ask Jayden, my creator\n\
```')

async def magic():
    await client.wait_until_ready()
    counter = 0
    magic = discord.Object(id='429243057557340171')
    while not client.is_closed:
        with urllib.request.urlopen("http://imgur.com/r/mtgaltered/hot.json") as url:
            data = json.loads(url.read().decode())
            var1 = data['data'][random.randint(0, len(data['data'])-1)]['hash']
            var2 = data['data'][random.randint(0, len(data['data'])-1)]['ext']
        await client.send_message(magic,'https://imgur.com/' + var1 + var2)
        time = 60 * 10
        await asyncio.sleep(time)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(magic())
client.run(TOKEN)
