import discord
import os
import psutil
import time
import datetime
from discord.ext import commands

start_time = time.time()

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(self,ctx, *users: discord.Member):
      if len(users) == 0:
        users = [ctx.message.author]
      for user in users:
        await ctx.send("Аватар `{0}`: {1}".format(user, user.avatar_url))
    
    @commands.command()
    async def status(self,ctx):
      
      seconds = time.time() - start_time
      m, s = divmod(seconds, 60)
      h, m = divmod(m, 60)
      d, h = divmod(h, 24)
      w, d = divmod(d, 7)
      if s != 0:
        msg = '**{0}** сек{1}.'.format(int(s), '' if m == 0 else '')
      if m != 0:
          e = '' if h == 0 else '.'
          msg = ' : **{0}** мин : '.format(int(m)) + msg.replace('.', '') + e
      if h != 0:
        e = '' if d == 0 else '.'
        msg = ' : **{0}** час : '.format(int(h)) + msg.replace('.', '') + e
      if d != 0:
        e = '' if w == 0 else '.'
        msg = ' : **{0}** день '.format(int(d)) + msg.replace('.', '').replace('', '') + e
      if w != 0:
        msg = ' : **{0}** год {1}'.format(int(w)) + msg.replace('.', '') + ''
      if m == 0:
        msg = ' '+msg
      else:
        msg = msg[2:]
      
      RAM = psutil.Process(os.getpid()).memory_full_info().rss / 1024**2
      ping = round(self.bot.latency * 1000, 1)
      
      embed = discord.Embed(title='Статус',color=discord.Color.dark_red())
      embed = embed.add_field(name="Время работы", value= f'Бот Online {msg}' ,inline=False)
      embed = embed.add_field(name="Использованно", value=f"{RAM:.2f} MB" ,inline=False)
      embed = embed.add_field(name= "Пинг", value= f"{int(ping)}ms",inline=False)
      await ctx.send(embed = embed)
    
    @commands.command()
    async def invite(self,ctx):
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Добавить меня к себе можно по этой ссылке", value='ссылка', inline=False)
      await ctx.send( embed = embed )

def setup(bot):
  bot.add_cog(Info(bot))
