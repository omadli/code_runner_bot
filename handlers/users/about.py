from aiogram import Router, types
from aiogram.filters import Command


router = Router()

@router.message(Command("about"))
async def cmd_help(msg: types.Message):
    await msg.reply(
        text="Taklif va murojaatlar uchun @murodillo17 yoki @MenTaLiST_VIP"
    )
