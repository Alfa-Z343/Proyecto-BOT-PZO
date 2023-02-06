from discord.ext import commands


class say_hello(commands.Cog, name='say_hello'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Says hello!')
	async def hello(self, ctx):
		await ctx.respond(f"hello, {ctx.author}")


def setup(bot):
	bot.add_cog(say_hello(bot))