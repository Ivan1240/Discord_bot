import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix="&", sync_commands_debug=True, test_guilds=[968372517326708786], intents=disnake.Intents.all())
client.remove_command('info')
client.remove_command('help')
tmr = '10 минут'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.command(aliases=['привет', 'ку', 'шалом', 'хай', 'салам', 'help', 'info' 'Привет', 'Ку', 'Шалом', 'Хай', 'Салам', 'Hello', 'Help'])
async def hello(ctx):
    emb = disnake.Embed(title="Ведутся технические работы.", description= "Через некоторое время бот возобновит свою работу. Приблизительное время ожидания: " + tmr, colour=disnake.Colour.yellow())
    await ctx.reply(embed=emb)

@client.command('info')
async def hello2(ctx):
    emb = disnake.Embed(title='Техн. работы', description = 'Что будет добавленно: \n   **Статус бота**\n\nПриблизительное время ожидания: ' + tmr, colour=disnake.Colour.yellow())
    await ctx.reply(embed=emb)

client.run("TOKEN")