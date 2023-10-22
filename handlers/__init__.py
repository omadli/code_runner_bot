from aiogram import Dispatcher

from handlers.admins import admin_router
from handlers.groups import group_router
from handlers.users import user_router
from handlers.codes import codes_router


def include_all_routers(dp: Dispatcher):
    dp.include_router(admin_router)
    dp.include_router(group_router)
    dp.include_router(user_router)
    dp.include_router(codes_router)
    