from discord.ext import commands


class faq3(commands.Cog, name='faq3'):
	def __init__(self, bot):
		self.bot = bot


	@commands.slash_command(description='Duda frecuente sobre los wipes y actividad del servidor')
	async def faq3(self, ctx):
		await ctx.respond(f"""
        Hola **{ctx.author}**, gracias por unirte a la comunidad de Project Zone Online.

        > __**Información sobre wipes y actividad del servidor**__
        > Los wipes en este servidor suelen durar entre 2, 3 o 4 meses, dependiendo de la actividad y las votaciones de los usuarios.
        > Cuando se va a realizar un wipe, se abre una votacion en el canal #votaciones, y dependiendo del resultado se inician preparativos

        > __**En inicios de wipe, ¿Hay actividad?**__
        > Si, generalmente cuanto mas reciente sea el wipe, mas actividad de usuarios suele haber, no obstante, no siempre se sigue este patrón.
        > A finales de wipe, la actividad suele ser mantenida por nuevos usuarios, y principalmente por eventos que lleva a cabo el staff.

        > __**¿Cuando fue el último wipe?**__
        > Generalmente cualquier usuario promedio puede resolverte esta duda, o cualquier administrador por cualquier canal o un ticket de duda.
        > En caso de que casualmente, no te responda nadie, puedes ir al canal #votaciones y buscar la fecha de la ultima votacion de wipe para aclarar la duda.
    """)


def setup(bot):
	bot.add_cog(faq3(bot))