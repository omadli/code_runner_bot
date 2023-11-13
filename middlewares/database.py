import time
import logging
from typing import Any, Awaitable, Callable, Dict, NamedTuple
from aiogram import BaseMiddleware, types

from db.models import DbUser
from utils.cache import cache


class CacheData(NamedTuple):
    last_event_time: float
    db_user: dict


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()
        
    def build_key(self, user_id: int|str):
        return "user" + str(user_id)
    
    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message, data: Dict[str, Any]) -> Any:
        user_id = event.from_user.id
        cache_data: CacheData|None = await cache.get(self.build_key(user_id), default=None)
        last_event_time = 0
        if cache_data is None: # None from cache
            db_user = await DbUser.get_or_none(id=user_id)
            if db_user is None: # None from db
                db_user = await DbUser.create(
                    id=user_id,
                    full_name=event.from_user.full_name,
                    username=event.from_user.username
                )
                await db_user.save()
            else: # not None from db
                if db_user.full_name != event.from_user.full_name or db_user.username != event.from_user.username:
                    logging.debug(db_user.full_name, event.from_user.full_name)
                    logging.debug(db_user.username, event.from_user.username)
                    db_user.full_name = event.from_user.full_name
                    db_user.username = event.from_user.username
                    await db_user.save()
        else: # not None from cache
            cache_data: CacheData
            last_event_time = cache_data.last_event_time
            db_user = cache_data.db_user
            
        await cache.set(self.build_key(user_id), CacheData(time.time(), dict(db_user)), ttl=2*60*60)
                
        data['db_user'] = dict(db_user)
        data['last_event_time'] = last_event_time
        
        return await handler(event, data)

