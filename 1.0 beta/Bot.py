import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix="&", sync_commands_debug=True, test_guilds=[968372517326708786], intents=disnake.Intents.all())
client.remove_command('help')
client.remove_command('info')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.slash_command(description="Команды")
async def cmds(inter):
    emb = disnake.Embed(title="Команды:", description="\nКу\nПривет\nДаров\nХай\nСалам\nШалом\nhelp\ninfo", colour=disnake.Colour.yellow())
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
    emb = disnake.Embed(title="Обо мне", description="\nПросто бот. Создан **@Bad Boy#4708** 05.05.2022. В даный момент нахдится на бета тесте на сервере AlexGyver community\n\nВерсия 1.0 beta", colour=disnake.Colour.red())
    view = disnake.ui.View()
    url = disnake.ui.Button(label='Мой github', url='https://github.com/Ivan1240/Discord_bot/')
    view.add_item(item=url)
    await ctx.reply(embed=emb, view=view)
    
client.run("TOKEN")
