from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart


router = Router()


@router.message(Command("help"))
@router.message(CommandStart(deep_link=True), F.text.endswith("help"))
async def cmd_help(msg: types.Message):
    await msg.reply(
        text="Bu bot sizga C++ Python Java kabi bir-necha dasturlash tillaridagi kodlaringizni compile/run qilib beradi😊\n"
            "Barcha dasturlash tillari ro'yxatini ko'rish uchun /languages buyrug'idan foydalaning.\n"
            "Har bir dasturlash tilining namunasiga qarab kodlaringizni yozishingiz mumkin.\n"
            "Bot input larni ham qo'llaydi.\n"
            "/stdin buyrug'idan keyingi qatoridan qator tashlab navbatma-navbat kiruvchi qiymatlarni kiritishingiz mumkin.\n"
            "Misol uchun (python dasturlash tilida):\n"
            "<code>/python</code>\n"
            "<pre><code class='language-python'>a = input()\n"
            "print(a)</code></pre>\n"
            "<code>/stdin\n"
            "Hello world</code>"
    )
