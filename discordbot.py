import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions

if __name__ == "__main__":
        
        load_dotenv()
        API_TOKEN = os.environ.get("API_TOKEN")

        bot=commands.Bot(command_prefix='.')
        @bot.event
        async def on_ready():
                print("We have logged in as {0.user}".format(bot))

        @bot.command()
        @commands.has_permissions(manage_messages=True)
        async def clear(ctx,amount=None):
                await ctx.channel.purge(limit=amount)
                
bot.run(API_TOKEN)
