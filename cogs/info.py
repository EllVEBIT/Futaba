import discord
import platform
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
          msg = '  **{0}** мин  '.format(int(m)) + msg.replace('.', '') + e
      if h != 0:
        e = '' if d == 0 else '.'
        msg = '  **{0}** час  '.format(int(h)) + msg.replace('.', '') + e
      if d != 0:
        e = '' if w == 0 else '.'
        msg = '  **{0}** день '.format(int(d)) + msg.replace('.', '').replace('', '') + e
      if w != 0:
        msg = '  **{0}** год {1}'.format(int(w)) + msg.replace('.', '') + ''
      if m == 0:
        msg = ' '+msg
      else:
        msg = msg[2:]
      
      RAM = psutil.Process(os.getpid()).memory_full_info().rss / 1024**2
      
      TRAM =psutil.virtual_memory().total / 1024**2
      
      ping = round(self.bot.latency * 1000, 1)
      
      embed = discord.Embed(title='Статус',color=discord.Color.dark_red())
      embed.add_field(name="Время работы", value= f'{msg}' ,inline=False)
      embed.add_field(name="Система", value=f"{platform.system()}",inline=False)
      embed.add_field(name="Ядер", value=f"{psutil.cpu_count()}",inline=True)
      embed.add_field(name="Используется", value=f"{RAM:.2f} MB" ,inline=True)
      embed.add_field(name="Всего", value=f"{TRAM:.2f} MB" ,inline=True)
      embed.add_field(name= "Пинг", value= f"{int(ping)} ms",inline=False)
      await ctx.send(embed = embed)
    
    @commands.command()
    async def invite(self,ctx):
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Добавить меня к себе можно по этой ссылке", value='https://discord.com/oauth2/authorize?client_id=737318737887232111&scope=bot&permissions=8', inline=False)
      await ctx.send( embed = embed )
    
    @commands.command()
    async def info(self,ctx, *users:discord.Member):
      if len(users) == 0:
        users = [ctx.message.author]
      for user in users:
        emb = discord.Embed(title='Информация о пользователе',color=discord.Color.dark_red())
        emb.add_field(name="Когда присоединился:",value=user.joined_at,inline=False)
        emb.add_field(name="Никнейм:",value=user.display_name,inline=False)
        emb.add_field(name="ID",value=user.id,inline= False)
        emb.add_field(name="Аккаунт был создан:",value=user.created_at.strftime("%#d %B %Y  %I:%M %p"),inline=False)
        roles = []
        for role in user.roles:
          if role.name != '@everyone':
            roles.append(role.mention)
        
        if len(roles) > 0:
          roles = ' , '.join(roles)
        else:
          roles = "Пользователь не имеет никаких ролей"
        
        emb.add_field(name="Роль", value=roles)
        emb.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed = emb)


def setup(bot):
  bot.add_cog(Info(bot))
