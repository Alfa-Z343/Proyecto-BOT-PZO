from discord.ext import commands


class faq4(commands.Cog, name='faq4'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Duda frecuente sobre configuración del servidor')
	async def faq4(self, ctx):
		await ctx.respond(f"""
        Hola **{ctx.author.mention}**, gracias por unirte a la comunidad de Project Zone Online.

        __**Información general sobre el servidor**__
        
        > Este servidor esta configurado en un nivel medio-dificíl. Los días duran actualmente 4 horas, 2 horas día y 2 horas noche.
        > El journal esta activado en el servidor, para recuperar un 25% de las habilidades totales transcritas.
        > La velocidad de los zombies estándar es de tambaleantes veloces, pero un 5% de todos los zombies son corredores. La infección solo se transmite por mordida.
        > La noche esta configurada en luminosidad normal, la temperatura esta un poco más fría que la estándar.
        > El respawn de loot esta activado semanalmente, pero depende de la última vez que jugadores estuvieran en la zona.
        > El fuego esta desactivado, unicamente en las hogueras esta presente, pero en ningún caso se expande para evitar el grieffing.
        > Los únicos comandos de chat activados son: /say, /yell y /all. En el chat /all, debe seguirse la normativa de discord al hablar.
        > Si deseas hablar en privado con otro jugador puedes usar una radio, y usar el voip o el chat /say.
        > **Recuerda: Si es tu primera vez en Project Zomboid, no recomendamos jugar en el servidor solo, porque tiene muchas características que no estan en el juego base**

        > __**¿Como funciona el respawn de ítems?**__
        > Ante todo aclarar dos cosas:
        > El respawn de loot, aunque esta configurado semanalmente, se reinicia el contador cada vez que un jugador este por la zona.
        > Por tanto, el staff no sabe con certeza cuando será el respawn. 
        > Puede que en algunos edificios sea semanalmente, y en otros tarde más por la presencia de jugadores.
        > **Explora el mapa y descubre tu mismo si hubo respawn o no**
    """)


def setup(bot):
	bot.add_cog(faq4(bot))
