from datetime import datetime, timedelta
from aiogram import types, Router
from aiogram.filters import Command

from db.models import DbUser
from settings import LANGUAGES


router = Router()

@router.message(Command("stat"))
async def cmd_ping(msg: types.Message):
    count_users = await DbUser.all().count()
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    tomorrow = today + timedelta(days=1)
    count_today_joined = await DbUser.filter(join_date__range=(today, tomorrow)).count()
    last_week = today - timedelta(days=7)
    count_last_week_joined = await DbUser.filter(join_date__range=(last_week, tomorrow)).count()
    last_month = today - timedelta(days=30)
    count_last_month_joined = await DbUser.filter(join_date__range=(last_month, tomorrow)).count()
    
    count_languages = len(LANGUAGES)
    
    await msg.answer(
        text=f"<b>📈Umumiy statistika📉</b>\n\n"
            f"Jami foydalanuvchilar: {count_users}\n"
            f"Bugun qo'shilganlar: {count_today_joined}\n"
            f"Oxirgi 1 haftada qo'shilganlar: {count_last_week_joined}\n"
            f"Oxirgi 1 oyda qo'shilganlar: {count_last_month_joined}\n\n"
            f"Jami foydalanish mumkin dasturlash tillari: {count_languages} ta"
    )
