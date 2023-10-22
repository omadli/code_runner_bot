from aiogram import Router

from .runner import router as runner_router
from .languages import router as languages_router

from middlewares.database import DatabaseMiddleware

codes_router = Router(name="Codes router")


codes_router.include_router(runner_router)
codes_router.include_router(languages_router)

codes_router.message.middleware.register(DatabaseMiddleware())
