from aiogram import Router, F
from settings import ADMINS

from .ping import router as ping_router
from .stat import router as stat_router


admin_router = Router(name="Admin router")

admin_router.message.filter(F.from_user.id.in_(ADMINS))

admin_router.include_router(ping_router)
admin_router.include_router(stat_router)
