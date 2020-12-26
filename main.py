import discord
from discord.ext import commands
import json
import download
from collections import defaultdict

TOKEN = 'NzczNDY2MzE5MjM2NDk3NDEw.X6JopA.ZPSDYzUXMpBJ84Jh2evzpS4ud5Q'
PREFIX = '/'
bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def covid(ctx,place=None):
    download.download()
    with open('COVID-19_data.json', 'r', encoding="utf-8") as json_open:
        json_load = json.load(json_open)
        jsn = json_load
        main_data = jsn[0]

    update = main_data['lastUpdate']
    virus_data = main_data['area']
    area_data = dict()
    for i in range(47):
        area = virus_data[i]['name_jp']
        how_many = virus_data[i]['npatients']
        area_data[area] = how_many
        

    if place == None:
        all_embed = discord.Embed(title='コロナウイルス累計感染者数',description='全国累計感染者数',colour=discord.Color.blue())
        for c in area_data.items():
            all_embed.add_field(name=c[0],value=f'{c[1]}名')
        all_embed.set_footer(text=f'最終更新:{update}',icon_url=ctx.author.avatar_url)
        await ctx.send(embed=all_embed)
        return
    else:
        places = area_data.keys()
        if place in places:
            covid_embed = discord.Embed(title='コロナウイルス累積感染者数',description=place,colour=discord.Color.blue())
            cv_many = area_data[place]
            covid_embed.add_field(name=place,value=f'{cv_many}名',inline=False)
            covid_embed.set_footer(text=f'最終更新:{update}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=covid_embed)
        else:
            await ctx.send('正式な都道府県名を入力してください。')




bot.run(TOKEN)