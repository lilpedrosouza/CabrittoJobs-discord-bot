import hikari
import lightbulb
from jobs_api import obter_vagas
import random

bot = lightbulb.BotApp(
    token="SEU_BOT_TOKEN_ID_AQUI",
    default_enabled_guilds=(1149771085085155509),
    intents=hikari.Intents.ALL,
    prefix="!"
)

@bot.command
@lightbulb.command("jobs", "Gera e mostra vagas.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def jobs(ctx: lightbulb.Context) -> None:

    job = ctx.event.message.content[len("!jobs ")::].strip()

    query = f'{job} no Brasil'
    page = random.randint(1, 3)
    num_pages = random.randint(1, 3)
    date_posted = 'month'
    remote_only = 'True'
    employment_types = 'fulltime, parttime, intern, contractor'

    embeds = await obter_vagas(query, page, num_pages, date_posted, remote_only, employment_types)

    if embeds:
        for embed in embeds:
            await ctx.respond(embed=embed)
    else:
        await ctx.respond("Erro ao obter informações de vagas.")

if __name__ == "__main__":
    bot.run()
