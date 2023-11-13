import time
import logging
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, types

from loader import bot


DEFAULT_RATE_LIMIT = 1


def rate_limit(limit: int, key=None):
    """
    Decorator for configuring rate limit and key in different functions.

    :param limit:
    :param key:
    :return:
    """

    def decorator(func):
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)
        return func

    return decorator


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: float = DEFAULT_RATE_LIMIT, key_prefix='antiflood_') -> None:
        self.rate_limit = limit
        self.prefix = key_prefix
        self.blockeds: Dict[str, float] = {}
        super().__init__()
        
    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message, data: Dict[str, Any]) -> Any:
        user_id:str = str(event.from_user.id)
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        
        last_event_time: float = data.get("last_event_time", 0)
        current_time: float = time.time()
        delta = current_time - last_event_time
        if delta < limit:
            # throttled
            if user_id in self.blockeds:
                self.blockeds[user_id] += delta
            else:
                self.blockeds[user_id] = current_time + delta
                await bot.send_sticker(
                    chat_id=user_id,
                    sticker="CAACAgEAAxkBAAEOog5iKxUXWqvqZRa4qDkHDxIM1XfWrwACTQEAAlEpDTmxB-uP2nlDiiME"
                )
                await bot.send_message(
                    chat_id=user_id,
                    text="To many requests!"
                )
            logging.info("Update cancelled: %s" % key)
            return
        else:
            if user_id in self.blockeds:
                delta2 = time.time() - self.blockeds[user_id]
                if delta2 < 0:
                    self.blockeds.pop(user_id)
                else:
                    logging.info("Update cancelled: %s" % key)
                    return
            return await handler(event, data)
        