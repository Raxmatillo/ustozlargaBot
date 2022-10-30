import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    users = await db.select_all_users()
    try:
        if str(message.from_user.id) not in str(users):
            await db.add_user(
                full_name=name,
                username=message.from_user.username,
                telegram_id=message.from_user.id
                )
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz!", reply_markup=menu)
    # Adminga xabar beramiz
    count = await db.count_users()
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)