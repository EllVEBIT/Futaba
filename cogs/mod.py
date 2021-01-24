import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MemberConverter

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        await ctx.send(f"{user.mention} был забанен(а)")


    @has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} был(а) выгнан(на)")


    @has_permissions(administrator=True)
    @commands.command()
    async def mute(self, ctx, user='all'):
        if user == 'all':

            if ctx.author.voice:
                for member in ctx.author.voice.channel.members:
                    await member.edit(mute=True)

                embed = discord.Embed(title=':white_check_mark: Участники были заглушенны',description=f"Участники в  `{ctx.author.voice.channel}` были заглушенны")
                await ctx.send(embed=embed)
            else:
                await ctx.send(':x: Вы должны быть в голосовом канале, что бы использовать эту команду')
        else:
            try:
                converter = MemberConverter()
                member = await converter.convert(ctx, user)
                if member.voice:
                    await member.edit(mute=True)
                    await ctx.send(":white_check_mark: Участник был заглушен")
                else:
                    await ctx.send("участник не находится в голосовом канале")
            except:
                await ctx.send(f"""Укажите пользователя, которого вы хотите отключить, или введите `all`, чтобы отключить всех в голосовом канале, к которому вы подключены по умолчанию все участники будут заглушенны""")


    @has_permissions(administrator=True)
    @commands.command()
    async def unmute(self, ctx, user='all'):
        if user == 'all':

            if ctx.author.voice:
                for member in ctx.author.voice.channel.members:
                    await member.edit(mute=False)

                embed = discord.Embed(title=':white_check_mark: Участники были отглушенны',description=f"Участники в `{ctx.author.voice.channel}` были отглушенны")
                await ctx.send(embed=embed)
            else:
                await ctx.send(':x: Вы должны быть в голосовом канале, что бы использовать эту команду')
        else:
            try:
                converter = MemberConverter()
                member = await converter.convert(ctx, user)
                if member.voice:
                    await member.edit(mute=False)
                    await ctx.send(":white_check_mark: Участник был отглушен")
                else:
                    await ctx.send("участник не находится в голосовом канале")
            except:
                await ctx.send(f"""Укажите пользователя, которого хотите включить, или введите `all`, что бы включить всех в голосовом канале, к которому вы подключены по умолчанию все участники будут отглушенны""")
  
    @has_permissions(manage_messages=True)
    @commands.command()
    async def warn(self, ctx, user: discord.Member = None, *, reason=None):
    
        if not reason:
            reason = 'неизвестно'
            
        embed = discord.Embed(title='Предупреждение',description=f'{user.mention} было выданно педупреждение пользователем {ctx.author.mention}')
        embed.add_field(name='причина:', value=reason)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

        embed = discord.Embed(title='Вам было выданно предупреждение', description=f'Пользователем {ctx.author.mention}')
        embed.add_field(name='причина:', value=reason)
        embed.set_thumbnail(url=user.avatar_url)
        await user.send(embed=embed)
    
    @has_permissions(administrator = True)
    @commands.command()
    async def clear(self,ctx,amount=10):
      deleted = await ctx.message.channel.purge(limit=amount +1)
      author = ctx.message.author
      await ctx.send(f'{ author.mention} удалил(а) несколько сообшений.')

def setup(bot):
  bot.add_cog(Moderation(bot))
