from aiogram import Router, types
from aiogram.filters import Command


router = Router()

@router.message(Command("help"))
async def cmd_help(msg: types.Message):
    await msg.reply(
        text="Bu bot sizga C++ Python Java kabi bir-necha dasturlash tillaridagi kodlaringizni compile/run qilib beradi😊"
    )
