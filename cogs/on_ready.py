from discord.ext import commands


class onStartup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has started up and is ready to receive commands.')


def setup(bot):
    bot.add_cog(onStartup(bot))