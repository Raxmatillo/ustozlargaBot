from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(
"""<b>❗️ Tarjima qilish uchun Qo'llanma! 📝</b>\n
Tarjima til kodi so'ng matnni yuboring
Til kodlari:
    /uz - o'zbekcha
    /en - inglizcha,
    /ru - ruscha,
    /ar - arabcha,
    /de - nemischa,
    /ko - koreyscha,
    /tr - turkcha\n,
<i>Misol uchun:</i>  /uz Hello World"""
        )