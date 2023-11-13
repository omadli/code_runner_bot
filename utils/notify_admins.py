import logging
from settings import ADMINS
from aiogram import Bot

async def startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin,
                text="Bot ishga tushdi"
            )
        except Exception as e:
            logging.exception(f"Admin: {admin} - {e}")
