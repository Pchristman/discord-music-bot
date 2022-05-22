import discord
from discord.ext import commands
import os
from music_cog import music_cog
from help_cog import help_cog

bot = commands.Bot(command_prefix='?')

bot.remove_command("help")

bot.add_cog(music_cog(bot))
bot.add_cog(help_cog(bot))

bot.run(os.getenv("TOKEN"))
# bot.run('OTc3OTc0MzY5NDUwMDY1OTUw.GFUtdd.h5L2SBKVNL2F6X8yvqnNF46dIsYGqcW7r3nSx0')