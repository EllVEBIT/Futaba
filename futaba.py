import discord
from discord.ext import commands
from discord.ext.commands import Bot
import waifu
import sys
import random
import asyncio
import time
import datetime
import re
import hello
import meme
import wikipedia

client = discord.Client()

client = commands.Bot( command_prefix = 'f!')

@client.event
async def on_ready():
    print('Мы вошли в систему как {0.user}'.format(client))

    await client.change_presence( status = discord.Status.online, activity = discord.Game('f!main') )

# меню команд

@client.command()
async def main(ctx):
	embed=discord.Embed(title="Основные команды", description="Префикс f!", color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
	embed.add_field(name="fate", value="Твоя вайфу из серии Fate.", inline=False)
	embed.add_field(name="info", value="Информация о любом пользователе на этом сервере.", inline=False)
	embed.add_field(name="clear", value="Для Админов и модераторов. Удаляет сообшения максимум 100.", inline=False)
	embed.add_field(name="'none'", value="скоро", inline=False)
	embed.add_field(name="'none'", value="скоро", inline=False)
	embed.add_field(name="'none'", value="скоро", inline=False)
	embed.add_field(name="'none'", value="none", inline=False)
	embed.add_field(name="'none'", value="none", inline=False)
	embed.add_field(name="'none'", value="none", inline=False)
	embed.add_field(name="'none'", value="скоро", inline=False)
	embed.set_footer(text="Создатель EvilBit#6696",icon_url='https://cdn.discordapp.com/avatars/552479599980970005/47b3832de0ae7f146822b319921baba5.png?size=1024')
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
@commands.has_permissions(view_audit_log=True)
async def clear(ctx,amount=100):
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

# роль для новичков

@client.event
async def on_member_join(member):
  hi = random.randint(0, 1 )
  
  channel = client.get_channel(751126851916660736)
  embed=discord.Embed(title="", description=f'{member.mention} Добро пожаловать!', color=0xff80ff)
  embed.set_image(url=hello.gifs[hi])
  
  await channel.send(embed=embed, content=None)
  
# мем

@client.command()
async def meme(ctx):
  mem = random.randint(0, 2 )
  
  embed=discord.Embed(color=0xff80ff)
  embed.set_image(url=meme.memeLinks[mem])
  
  await ctx.send(embed=embed, content=None)
 
  await channel.send(embed=embed, content=None) 
  
# Твой токен
client.run('токен')
