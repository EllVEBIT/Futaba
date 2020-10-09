import discord
from discord.ext import commands
from discord.ext.commands import Bot
from aiohttp import request
import sys
import os
import random
import asyncio
import time
import datetime
import re
import wikipedia
import waifu
import nekos
import json
import io
from time import strftime
from bs4 import BeautifulSoup
from discord.ext.commands import has_permissions, CheckFailure

client = commands.Bot( command_prefix = 'f!')

status = ['f!main', 'Версия 0.0.1', 'Хостинг Heroku']

@client.event
async def on_ready():
    print('вы вошли в систему как {0.user}'.format(client))

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

# ошибки и сообшения
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Такой команды нет, либо команда написанна неправильно. Чтобы посмотреть список доступных команд введите```f!main```')
    
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('Данная команда доступна только Администраторам!')

@client.command()
async def creator(ctx):
  author = ctx.message.author
  embed = discord.Embed(color=0xff80ff)
  embed.set_author(name="Информация")
  embed.add_field(name="Создатель:", value='Elin#6696', inline=False)
  embed.add_field(name="Исходный код", value='https://github.com/EllVEBIT/Futaba', inline=False)
  embed.add_field(name="Добавить к себе", value='https://discord.com/oauth2/authorize?client_id=737318737887232111&scope=bot&permissions=8', inline=False)
  embed.add_field(name="Контакты", value='https://vk.com/evilbitsd', inline=False)
  embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/552479599980970005/bd0258cf2634b8426c7e175c0ea97ab7.webp?size=1024')
  
  await ctx.send(embed=embed)

# меню

@client.command()
async def main(ctx):
	embed=discord.Embed(title="Основные команды", description="Префикс f!", color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
	embed.add_field(name="Fun", value="info, fate, neko_gif, kiss, avatar, feed", inline=False)
	embed.add_field(name="Admin", value="clear, say", inline=False)
	embed.add_field(name="NSFW", value="wallpaper, erokemo, cum", inline=False)
	embed.add_field(name="System", value="creator, ping", inline=False)
	embed.set_footer(text="Создатель @Elin#6696",icon_url='https://cdn.discordapp.com/avatars/552479599980970005/bd0258cf2634b8426c7e175c0ea97ab7.png?size=1024')
	await ctx.send(embed=embed)

# информация о пользователе

@client.command()
async def info(ctx,member:discord.Member):
  emb = discord.Embed(title='Информация о пользователе',color=0xff80ff)
  emb.add_field(name="Когда присоединился:",value=member.joined_at,inline=False)
  emb.add_field(name="Никнейм:",value=member.display_name,inline=False)
  emb.add_field(name="ID",value=member.id,inline= False)
  emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%#d %B %Y  %I:%M %p"),inline=False)
  emb.set_thumbnail(url=member.avatar_url)
  await ctx.send(embed = emb)

# avatar пользователя любого  

@client.command()
async def avatar(ctx,member:discord.Member):
   emb = discord.Embed()
   emb.set_image(url=member.avatar_url)
   await ctx.send(embed = emb)

# для Админов 
###########################################
# очистка сообшений для админов

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx,amount=2000):
  deleted = await ctx.message.channel.purge(limit=amount +1)
  author = ctx.message.author
  await ctx.send(f'{ author.mention} удалил(а) несколько сообшений.')

# пинг

@client.command()
async def ping(ctx):
  await ctx.send(f"Пинг {round(client.latency * 1000)}ms")

# wiki

@client.command()
async def wiki(ctx, *, text):
    wikipedia.set_lang("ru")
    new_page = wikipedia.page(text)
    summ = wikipedia.summary(text)
    emb = discord.Embed(
        title= new_page.title,
        description= summ,
         color=0xff80ff
    )
    emb.set_author(name= 'Wikipedia', url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
 
    await ctx.send(embed=emb)

# написать от лица бота (только дя админов)

@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, *, msg):
  await ctx.message.delete()
  await ctx.send("{}" .format(msg))

#Fun
###########################################
# neko_gif

@client.command()
async def neko_gif(ctx):
    embed = discord.Embed(
        title='',
        description='',
        timestamp=datetime.datetime.utcnow(), color=0xff80ff)
    ngif = nekos.img("ngif")
    embed.set_image(url=ngif)
    embed.set_footer(text=f"Попросил(а): {ctx.author.name}")

    await ctx.send(embed=embed)

# твоя вайфу из серий Fate

@client.command()
async def fate(ctx):
  chosen_index = random.randint(0, 409 )
  
  embed = discord.Embed(title=waifu.waifuName[chosen_index], description=waifu.waifuSeries[chosen_index], timestamp=datetime.datetime.utcnow(), color=0xff80ff)
  embed.set_image(url=waifu.waifuLinks[chosen_index])
  embed.set_footer(text=f"Попросил(а): {ctx.author.name}")
  
  await ctx.send(content=None, embed=embed)

# kiss

@client.command()
async def kiss(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} Поцеловал(а) {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    kiss = nekos.img("kiss")

    embed.set_image(url=kiss)

    await ctx.send(embed=embed)

@client.command()
async def feed(ctx):
    embed = discord.Embed(
        title='',
        description='',
        timestamp=datetime.datetime.utcnow(), color=0xff80ff)
    feed = nekos.img("feed")
    embed.set_image(url=feed)
    embed.set_footer(text=f"Попросил(а): {ctx.author.name}")

    await ctx.send(embed=embed)

#Nsfw 
###########################################
# erokemo

@client.command()
async def erokemo(ctx):
    if not ctx.channel.is_nsfw():
      author = ctx.message.author
      await ctx.send("Такие штучки работают только в NSFW каналах!")
      sys.stderr = object
    if ctx.channel.is_nsfw():
        embed = discord.Embed(
            title='',
            description='',
            timestamp=datetime.datetime.utcnow(), color=0xff80ff
        )
    erokemo = nekos.img("erokemo")
    embed.set_image(url=erokemo)
    embed.set_footer(text=f"Попросил(а): {ctx.author.name}")

    await ctx.send(embed=embed)

# walpapper

@client.command()
async def wallpaper(ctx):
    if not ctx.channel.is_nsfw():
      author = ctx.message.author
      await ctx.send("Такие штучки работают только в NSFW каналах!")
      sys.stderr = object
    if ctx.channel.is_nsfw():
        embed = discord.Embed(
            title='',
            description='',
            timestamp=datetime.datetime.utcnow(), color=0xff80ff)
    wallpaper = nekos.img("wallpaper")
    embed.set_image(url=wallpaper)
    embed.set_footer(text=f"Попросил(а): {ctx.author.name}")
    
    await ctx.send(embed=embed)

# cum

@client.command()
async def cum(ctx):
    if not ctx.channel.is_nsfw():
      author = ctx.message.author
      await ctx.send("Такие штучки работают только в NSFW каналах!")
      sys.stderr = object
    if ctx.channel.is_nsfw():
        embed = discord.Embed(
            title='',
            description='',
            timestamp=datetime.datetime.utcnow(), color=0xff80ff)
    cum = nekos.img("cum")

    embed.set_image(url=cum)
    embed.set_footer(text=f"Попросил(а): {ctx.author.name}")
    
    await ctx.send(embed=embed)

token = os.environ.get('BOT_TOKEN') 

# Твой токен
client.run(str(token))
