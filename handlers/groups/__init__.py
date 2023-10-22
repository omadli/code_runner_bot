from aiogram import Router, F

from middlewares.database import DatabaseMiddleware

group_router = Router(name="Group router")

group_router.message.filter(F.chat.type.in_(["group", "supergroup"]))

group_router.message.middleware.register(DatabaseMiddleware())
