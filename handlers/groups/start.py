from aiogram import Router, types, enums
from aiogram.filters import CommandStart

from loader import bot

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: types.Message):
    await msg.reply(
        text=f"Assalomu alaykum {msg.from_user.mention_html()}"
    )
    res: types.ChatMember = await bot.get_chat_member(
        chat_id=msg.chat.id,
        user_id=bot.id
    )
    if res.status != enums.chat_member_status.ChatMemberStatus.ADMINISTRATOR:
        # bot admin emas guruhda
        await msg.answer("Guruhda mendan to'liq foydalanish uchun meni admin qiling")
        await msg.answer_sticker("CAACAgIAAxkBAAEXIDZlO4AgH4l7MVWzOwpRvwABIVArWgsAAukdAAIZMshLRr0YDfbrKiAwBA")
