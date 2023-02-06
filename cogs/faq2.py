from discord.ext import commands


class faq2(commands.Cog, name='faq2'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Duda frecuente sobre como jugar con otra gente')
	async def faq2(self, ctx):
		await ctx.respond(f"""
        Hola **{ctx.author.mention}**, gracias por unirte a la comunidad de Project Zone Online.

        > __**Respuesta a las preguntas: ¿Alguien juega? ¿Juegan project zomboid en este servidor?**__
        > Si, hay numerosos usuarios que juegan en este servidor, tanto en el servidor ingame de project zomboid, como cooperativos entre ellos.
        > En el canal autoroles puedes reclamar roles según lo que busques en este servidor, cooperativo o servidor ingame.

        > __**Ya he hecho lo anterior, ¿Que hago ahora?**__
        > Tras completar los pasos anteriores, puedes acceder tanto al servidor ingame, (Comando faq_1 si no sabes como) o buscar una partida cooperativa.
        > Las partidas cooperativas se buscan en el canal #Busco-Partida, que será visible cuando reclames el rol cooperativo.

        > __**Recuerda:**__
        > Para entrar al servidor ingame debes leer la normativa del servidor para evitar warns innecesarios.
        > Las partidas cooperativas que encuentres en #Busco-Partida, son propiedad del usuario que las abra, y no estan vinculadas a las normas o staff de este servidor.
    """)


def setup(bot):
	bot.add_cog(faq2(bot))
