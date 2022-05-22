import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix="&", sync_commands_debug=True, test_guilds=[968372517326708786], intents=disnake.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.command(aliases=['привет', 'ку', 'шалом', 'хай', 'салам', 'help', 'info', 'Привет', 'Ку', 'Шалом', 'Хай', 'Салам', 'Hello', 'Help', 'Info'])
async def hello(ctx):
    emb = disnake.Embed(title="Ведутся технические работы.", description= "Через некоторое время бот возобновит свою работу. Приблизительное время ожидания 10 минут.", colour=disnake.Colour.yellow())
    await ctx.reply(embed=emb)
    
client.run("TOKEN")
