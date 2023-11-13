from time import time
from aiogram import types, Router
from aiogram.filters import Command


router = Router()

@router.message(Command("ping"))
async def cmd_ping(msg: types.Message):
    t1 = time()
    m = await msg.reply("Pong!")
    t2 = time()
    ping_time = round((t2 - t1) * 1000)
    await m.edit_text(f"🚀Ping: {ping_time} ms")

