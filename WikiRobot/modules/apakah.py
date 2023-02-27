import random
from WikiRobot.events import register
from WikiRobot import telethn

APAKAH_STRING = [
    "Iya",
    "Tidak",
    "Mungkin",
    "Mungkin Tidak",
    "Bisa jadi",
    "Mungkin Tidak",
    "Tidak Mungkin",
    "YNTKTS",
    "Pala bapak kau pecah",
    "Apa iya?",
    "Alhamdulillah 😑" "Tanya aja sama mamak kau tu pler",
]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("Berikan saya pertanyaan 😑")
        return
    await event.reply(random.choice(APAKAH_STRING))
