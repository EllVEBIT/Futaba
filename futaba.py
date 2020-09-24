import discord
from discord.ext import commands
from discord.ext.commands import Bot
from aiohttp import request
import sys
import random
import asyncio
import time
import datetime
import re
import wikipedia
import waifu
import hello
import json
import meme
import asyncio
import json
from time import strftime
from bs4 import BeautifulSoup

client = discord.Client()

client = commands.Bot( command_prefix = 'f!')

@client.event
async def on_ready():
    print('вы вошли в систему как {0.user}'.format(client))

    await client.change_presence( status = discord.Status.online, activity = discord.Game('f!main') )

# ошибки

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Такой команды нет, чтобы посмотреть список доступных команд введите f!main')
    
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('Данная команда доступна только Администраторам!')

# меню

@client.command()
async def main(ctx):
	embed=discord.Embed(title="Основные команды", description="Префикс f!", color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
	embed.add_field(name="fate", value="Твоя вайфу из серии Fate.", inline=False)
	embed.add_field(name="info", value="Информация о любом пользователе на этом сервере.", inline=False)
	embed.add_field(name="clear", value="Для Админов и модераторов. Удаляет сообшения максимум 100.", inline=False)
	embed.add_field(name="wiki", value="Поиск в wikipedia", inline=False)
	embed.add_field(name="mem", value="Разные мемы", inline=False)
	embed.add_field(name="'none'", value="скоро", inline=False)
	embed.add_field(name="'none'", value="none", inline=False)
	embed.add_field(name="'none'", value="none", inline=False)
	embed.add_field(name="'none'", value="none", inline=False)
	embed.add_field(name="'none'", value="скоро", inline=False)
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

# очистка сообшений для админов

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx,amount=2000):
  deleted = await ctx.message.channel.purge(limit=amount +1)
  author = ctx.message.author
  await ctx.send(f'{ author.mention} удалил(а) несколько сообшений.')

# твоя вайфу из серий Fate

@client.command()
async def fate(ctx):
  chosen_index = random.randint(0, 409 )
  
  embed = discord.Embed(title=waifu.waifuName[chosen_index], description=waifu.waifuSeries[chosen_index], timestamp=datetime.datetime.utcnow(), color=0xff80ff)
  embed.set_image(url=waifu.waifuLinks[chosen_index])
  embed.set_footer(text=f"Попросил(а): {ctx.author.name}")
  
  await ctx.send(content=None, embed=embed)

# приветсвие для участников

@client.event
async def on_member_join(member):
  hi = random.randint(0, 1 )
  
  channel = client.get_channel(751126851916660736)
  embed=discord.Embed(title="", description=f'{member.mention} Добро пожаловать!', color=0xff80ff)
  embed.set_image(url=hello.gifs[hi])
  
  await channel.send(embed=embed, content=None)

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
  
# мем

@client.command()
async def mem(ctx):
  me = random.randint(0, 8 )
  
  embed=discord.Embed(timestamp=datetime.datetime.utcnow(), color=0xff80ff)
  embed.set_image(url=meme.memesLinks[me])
  embed.set_footer(text=f"Попросил(а): {ctx.author.name}")
 
  await ctx.send(embed=embed, content=None)

# написать от лица бота (только дя админов)

@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, *, msg):
  await ctx.message.delete()
  await ctx.send("{}" .format(msg))
  
# Твой токен
client.run('токен')
