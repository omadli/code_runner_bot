import logging
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


from settings import BOT_TOKEN, DEBUG
from handlers import include_all_routers
from utils.startup import on_startup

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(
    storage=MemoryStorage()
)

log_level = logging.INFO
if DEBUG:
    log_level = logging.DEBUG

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=log_level,
)

include_all_routers(dp)


async def main():
    await on_startup(dp, bot)
    logging.info("Bot started")
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
