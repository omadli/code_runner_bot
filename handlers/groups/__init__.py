from aiogram import Router, F

from middlewares.database import DatabaseMiddleware
from .start import router as start_router
from .status_updated import router as status_updated_router

group_router = Router(name="Group router")

group_router.message.filter(F.chat.type.in_(["group", "supergroup"]))

group_router.message.middleware.register(DatabaseMiddleware())

group_router.include_router(start_router)
group_router.include_router(status_updated_router)
