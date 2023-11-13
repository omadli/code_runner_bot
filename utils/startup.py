from aiogram import Bot, Dispatcher, types
from tortoise import Tortoise
from settings import DB_URL

from utils.notify_admins import startup_notify


async def on_startup(dp: Dispatcher, bot: Bot):
    await bot.set_my_commands(
        commands=[
            types.BotCommand(command="start", description="Boshlash"),
            types.BotCommand(command="help", description="Yordam"),
            types.BotCommand(command="about", description="Dasturchi haqida"),
            types.BotCommand(command="languages", description="Barcha dasturlash tillari"),
        ]
    )
    await startup_notify(bot)
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['db.models', 'aerich.models']}
    )
    