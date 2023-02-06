from discord.ext import commands


class faq1(commands.Cog, name='faq1'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Duda frecuente sobre como entrar al servidor')
	async def faq1(self, ctx):
		await ctx.respond(f"""
        Hola **{ctx.author}**, gracias por unirte a la comunidad de Project Zone Online.

        > __**La pregunta clásica: ¿Como me uno al servidor?**__
        > Antes de pensar siquiera en unirte al servidor ingame, por favor recuerda reclamar el rol servidor ingame en el canal de autoroles
        > Posteriormente lee la normativa del servidor que será visible tras completar el paso anterior.

        > __**Ya he hecho lo anterior, ¿Como entro al servidor?**__
        > Tras completar los pasos anteriores, puedes acceder directamente al servidor desde este link: steam://connect/158.69.54.172:16261
        > El servidor no tiene contraseña. En nombre de usuario debes poner tu nombre en este servidor de discord, y la contraseña que quieras.

        > __**Recuerda estar pendiente de las actualizaciones de normativa**__
        > El no conocer la normativa no te exime de cumplirla.
        > Si tienes dudas, el staff siempre atiende en los tickets del canal #tickets o en el canal #dudasyayuda.
    """)


def setup(bot):
	bot.add_cog(faq1(bot))