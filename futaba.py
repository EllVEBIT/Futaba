import os
from pathlib import Path
import random
from random import choice
import time
import json
import datetime
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

config = {}
with open('config.json', 'r') as f:
	config = json.load(f)

bot = commands.Bot( command_prefix=(config['prefix']), owner_id=(config['owner']))

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

ltime = time.asctime(time.localtime())

@bot.event
async def on_ready():
    change_status.start()
    print(f'[INFO {ltime}]: Вы вошли как {bot.user.name}!')

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(config['status'])))

if __name__ == '__main__':
  bot.run(config['token'])
