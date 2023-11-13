from aiogram import Router, types, F


router = Router()

@router.message(F.text)
async def unknown_handler(msg: types.Message):
    await msg.reply(
        text="Noma'lum buyruq!"
    )
