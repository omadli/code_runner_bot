from aiogram import Router, types
from aiogram.filters import Command

from settings import LANGUAGES

router = Router()

@router.message(Command("languages"))
async def cmd_languages(msg: types.Message):
    txt = "\n".join([f"/{lang['command']:<8} - {lang['name'].title()}   v{lang['version']}" for lang in LANGUAGES.values()])
    await msg.reply(
        text=f"Barcha foydalanish mumkin bo'lgan dasturlash tillari ro'yxati:\n{txt}"
    )

