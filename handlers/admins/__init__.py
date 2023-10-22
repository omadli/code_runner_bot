from aiogram import Router, F
from settings import ADMINS

admin_router = Router(name="Admin router")

admin_router.message.filter(F.from_user.id.in_(ADMINS))
