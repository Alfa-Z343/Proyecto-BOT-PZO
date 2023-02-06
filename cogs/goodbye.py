from discord.ext import commands


class say_goodbye(commands.Cog, name='say_goodbye'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Says goodbye!')
	async def goodbye(self, ctx):
		await ctx.respond(f"goodbye, {ctx.author}")


def setup(bot):
	bot.add_cog(say_goodbye(bot))