import logging
from aiogram import Router, types

from loader import bot

router = Router()

@router.chat_member()
async def status_updated(event: types.ChatMemberUpdated):
    logging.debug(event)
    logging.debug(event.model_dump_json(indent=4))
    