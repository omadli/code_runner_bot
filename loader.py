from aiogram import Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(
    storage=MemoryStorage()
)

