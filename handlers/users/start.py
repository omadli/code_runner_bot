from aiogram import Router, types
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart(deep_link=False))
async def cmd_start(msg: types.Message):
    await msg.reply(
        text=f"Assalomu alaykum {msg.from_user.mention_html()}"
    )
