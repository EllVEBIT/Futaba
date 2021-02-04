import discord
import json
import random, requests
from discord.ext import commands

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True, aliases=['r34','34'])
    async def rule34(self, ctx, *, tags:str):
      if not ctx.channel.is_nsfw():
        await ctx.send("Такие штучки работают только в NSFW каналах!")
      if ctx.channel.is_nsfw():
        await ctx.channel.trigger_typing()
        try:
          data = requests.get("http://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags={}".format(tags)).json()
        except json.JSONDecodeError:
          await ctx.send("Ничего ненайдeнно по этому тегу: {} ".format(tags))
          return
        
        count = len(data)
        image_count = 1
        if count < 1:
          image_count = count
        images = []
        for i in range(image_count):
          image = data[random.randint(0, count)]
          images.append("http://img.rule34.xxx/images/{}/{}".format(image["directory"], image["image"]))
          result = "".join(images)
        
        embed=discord.Embed(color=discord.Color.dark_red(),title="Rule34: {}".format(tags),description=f"[Нет изображения, нажми сюда]({result})")
        embed.set_image(url=result)
        embed.set_footer(text="Теги: {}".format(image['tags']))
        await ctx.send(embed=embed)
        
def setup(bot):
  bot.add_cog(NSFW(bot))
