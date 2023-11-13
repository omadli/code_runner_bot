import logging
import asyncio

from loader import bot, dp
from settings import DEBUG
from utils.startup import on_startup
from handlers import include_all_routers
from middlewares.logging_updates import LoggingUpdatesMiddleware


log_level = logging.INFO
if DEBUG:
    log_level = logging.DEBUG
    dp.update.middleware.register(LoggingUpdatesMiddleware())

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
