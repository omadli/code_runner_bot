import logging
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, types

from db.models import DbUser
from utils.cache import cache


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()
    
    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message, data: Dict[str, Any]) -> Any:
        user_id = event.from_user.id
        db_user: DbUser|None = await cache.get("user" + str(user_id), default=None)
        if db_user is None:
            db_user = await DbUser.get_or_none(id=user_id)
            if db_user is not None:
                await cache.set("user" + str(user_id), db_user, ttl=2*60*60)
            
        if db_user is None:
            db_user = await DbUser.create(
                id=user_id,
                full_name=event.from_user.full_name,
                username=event.from_user.username
            )
            await db_user.save()
            await cache.set("user" + str(user_id), db_user, ttl=2*60*60)
        else:
            if db_user.full_name != event.from_user.full_name or db_user.username != event.from_user.username:
                logging.debug(db_user.full_name, event.from_user.full_name)
                logging.debug(db_user.username, event.from_user.username)
                db_user.full_name = event.from_user.full_name
                db_user.username = event.from_user.username
                await db_user.save()
                await cache.set("user" + str(user_id), db_user, ttl=2*60*60)
                
        data['db_user'] = db_user
        
        return await handler(event, data)

