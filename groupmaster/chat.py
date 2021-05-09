import random

from nonebot import on_command

from hoshino import R, Service, priv, util


#basic function for debug, not included in Service('chat')

@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')

@on_command('废材萝卜子', aliases=('废物萝卜子'), only_to_me=True)
async def robot_bi(session):
    await session.send('哔——把机器人称为废物违反了反歧视法！' + R.img("吹哨.png").cqcode)
    
    
#@on_command('zai?', aliases=('废材萝卜子'), only_to_me=True)
#async def seina(bot, ev):
#    await bot.send(ev, R.img('吹哨.jpg').cqcode)


sv = Service('chat', visible=False)

#@sv.on_fullmatch('沙雕','垃圾','辣鸡','傻逼','zz','智障')
#async def say_sorry(bot, ev):
#    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo','亲爱的'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('我不是你老婆.jpg').cqcode)
    else:
        await bot.send(ev, 'mua~')


@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '变态桑太变态了！我不是这样的人！', at_sender=True)


@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '我要报警了哦！', at_sender=True)


@sv.on_fullmatch('来点xcw')
async def seina(bot, ev):
    await bot.send(ev, R.img('xcw.png').cqcode)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', '我朋友好了'))
async def ddhaole(bot, ev):
    await bot.send(ev, '你说的这个朋友，是不是你自己？')
    await util.silence(ev, 30)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    await util.silence(ev, 30)


# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.1:
        await bot.send(ctx, R.img(f"确实{random.randint(1, 3)}.jpg").cqcode)


@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.1:
        await bot.send(ctx, R.img('我的天啊你看看都几点了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.1:
        await bot.send(ctx, R.img('内鬼.png').cqcode)


nyb_player = f'''{R.img('newyearburst.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()


@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.1:
        await bot.send(ev, nyb_player)
