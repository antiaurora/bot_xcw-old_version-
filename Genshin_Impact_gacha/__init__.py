from hoshino import Service
from .gacha import gacha_10 , gacha_90 , gacha_info

sv = Service('原神抽卡')


@sv.on_prefix('原神十连')
async def gacha_(bot, ev):
    await bot.send(ev, gacha_10() , at_sender=True)

@sv.on_prefix('原神半井')
async def gacha_(bot, ev):
    await bot.send(ev, gacha_90(90) , at_sender=True)

@sv.on_prefix('原神一井')
async def gacha_(bot, ev):
    await bot.send(ev, gacha_90(180) , at_sender=True)

@sv.on_prefix(["原神卡池","原神up","原神UP"])
async def gacha_(bot, ev):
    await bot.send(ev, gacha_info() , at_sender=True)



#@sv.on_prefix('垃圾原神')
#async def nihaole(bot, ev):
#    await bot.send(ev, gacha_90(90) , at_sender=True)
    
@sv.on_fullmatch('一二三四五六七七')
async def nihaole(bot, ev):
    await bot.send(ev, '一二三四五六七七')
    await util.silence(ev, 30)