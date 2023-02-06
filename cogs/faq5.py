from discord.ext import commands


class faq5(commands.Cog, name='faq5'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Dudas frecuentes sobre problemas ingame')
	async def faq5(self, ctx):
		await ctx.respond(f"""
        Hola **{ctx.author.mention}**, gracias por unirte a la comunidad de Project Zone Online.

        > __**Problemas típicos Ingame:**__
        
        > "Mi personaje se esta mareando y no estoy infectado, ni me atacó ningún zombie":
        > El mareo tiene diversas causas: 
        > 1º Revisa que no has tomado ningún alimento en mal estado.
        > 2º Revisa que tu fuente de agua, es potable. (Advertencia: El indicador de agua no potable esta desactivado en el servidor, hierve tu agua en caso de duda)
        > 3º No estés cerca de cadáveres mucho tiempo, y evita comer cerca de cadáveres.
        
        > "Mi coche no enciende, y tiene gasolina y todo bien":
        > Aunque en algunos casos puede ser por bug, la mayoría de estos reportes son debidos a que la batería del coche no tiene carga.
        > Al poner tu cursor encima de la batería en la interfaz de mecánica, podrás ver si tiene batería o no.
        > Para ahorrarnos trabajo al staff, evita por favor abrir ticket antes de comprobar lo anterior ¡Gracias!

        > "El interior de mi refugio no se detecta como interior, aunque esta todo cerrado":
        > Este problema suele ser por el bugeo de alguna pared, generalmente, cerca de una escalera que esta mal colocada.
        > Generalmente si aislas la sala de la escalera, el problema suele solucionarse, no obstante no siempre es así.
        > En caso de que esto no te funcione, y tras haber comprobado que todo tu refugio esta cerrado, abre un ticket de soporte y te atenderemos lo antes posible. 
    """)


def setup(bot):
	bot.add_cog(faq5(bot))
