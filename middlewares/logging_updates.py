import logging
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, types

class LoggingUpdatesMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        
    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message, data: Dict[str, Any]) -> Any:
        logging.debug(event.model_dump_json(indent=4))
        return await handler(event, data)
    