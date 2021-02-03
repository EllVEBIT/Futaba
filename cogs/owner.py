import discord
import subprocess
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def logout(self,ctx):
      await ctx.send("Выключение...")
      await ctx.bot.logout()
    
    @commands.command()
    @commands.is_owner()
    async def say(self,ctx, *, msg):
      await ctx.message.delete()
      await ctx.send("{}" .format(msg))
    
    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(send_messages=True, manage_messages=True)
    async def sayall(self,ctx, channel:discord.TextChannel, *msg):
      message = " ".join(msg)
      await channel.send(message)
    
    @commands.command()
    @commands.is_owner()
    async def term(self,ctx, *, command:str):
      process = subprocess.Popen(command.split(), stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
      await ctx.send(f"```{process}```")
      
def setup(bot):
  bot.add_cog(Owner(bot))
