from aiogram import Router

from settings import LANGUAGES
from utils.code_runner import run_in_message


router = Router()

for name, lang in LANGUAGES.items():
    run_in_message(lang, router)

