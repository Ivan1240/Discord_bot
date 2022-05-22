import disnake
from disnake.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix="&", sync_commands_debug=True, test_guilds=[968372517326708786], intents=disnake.Intents.all())
client.remove_command('help')
client.remove_command('info')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.slash_command(description="Команды")
async def cmds(inter):
    emb = disnake.Embed(title="Команды:", description="\n&Ку\n&Привет\n&Даров\n&Хай\n&Салам\n&Шалом\n&help\n&info", colour=disnake.Colour.yellow())
    await inter.response.send_message(embed=emb)

@client.command(aliases=['привет', 'ку', 'шалом', 'хай', 'салам', 'Привет', 'Ку', 'Шалом', 'Хай', 'Салам', 'Hello'])
async def hello(ctx):
    await ctx.reply("И тебе привет!")

@client.command(aliases=['help'])
async def hello1(ctx):
    emb = disnake.Embed(title="Нужна помощь? Я откликаюсь на:", description="\n&Привет\n&Всем привет\n&Ку\n&Хай\n&Даров\n&Салам\n&Прив\n&Шалом", colour=disnake.Colour.yellow())
    await ctx.reply(embed=emb)

@client.command(aliases=['info'])
async def hello2(ctx):
    emb = disnake.Embed(title="Обо мне", description="\nПросто бот. Создан **@Bad Boy#4708** 05.05.2022.\n\nВерсия 1.1 actual", colour=disnake.Colour.red())
    view = disnake.ui.View()
    url = disnake.ui.Button(emoji='⚔', label='Мой github', url='https://github.com/Ivan1240/Discord_bot/')
    view.add_item(item=url)
    await ctx.reply(embed=emb, view=view)
    
keep_alive()
client.run("TOKEN")
