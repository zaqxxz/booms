import discord
import os
import asyncio
from discord.ext import commands
import asyncio


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help cmd work")
        
    @commands.command(pass_context=True)
    async def help(self, ctx, *cog):

      embed = discord.Embed(
        colour = discord.Colour.default()
      )
    
      embed.add_field(name='help', value='gives you this msg right here.', inline=True)
      embed.add_field(name='moderation', value='gives you a list of mod cmds we have.', inline=True)
      embed.add_field(name='utility', value='gives you a list of util cmds we have.', inline=True)
      embed.add_field(name='fun', value='gives you a list of fun cmds we have.', inline=True)
      embed.add_field(name='support', value='shows the dev discord tag for you to add if you have any problems.', inline=True) 
      embed.set_image(url="https://images-ext-1.discordapp.net/external/T7sWSm4BiX5ebciMJyaQfOIjJHyLChEwu_P--g9aqRk/https/media.discordapp.net/attachments/859883140423614474/859883158493593600/dividerrr.gif")

      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))