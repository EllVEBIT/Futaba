import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.NotOwner):
      await ctx.send('Данная команда доступна только владельцу бота')
        
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

def setup(bot):
  bot.add_cog(Owner(bot))
