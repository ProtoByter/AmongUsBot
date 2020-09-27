import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def getPrefix():
    with open("./conf.txt","r") as conf:
        lines = conf.readlines()
        return lines[0]

def setPrefix(newPrefix):
    replace_line("conf.txt",0,newPrefix+"\n")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(getPrefix()):
        if message.content[1:7] == "prefix":
            prefix = message.content[8:]
            setPrefix(prefix)
            await message.channel.send(f'Prefix set to {prefix}')

client.run(TOKEN)