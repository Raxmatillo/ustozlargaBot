import asyncio
from filters import IsAdmin
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.dashboardKeyboard import admin_keyboards

from data.config import ADMINS
from states.AdminState import ReklamaState
from loader import dp, db, bot

@dp.message_handler(IsAdmin(), text="/admin")
async def admin_panel(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users, reply_markup=admin_keyboards)

@dp.message_handler(IsAdmin(), text="📌 Reklama")
async def send_ad_to_all(message: types.Message):
    await message.answer("Reklamani Menga yuboring")
    await ReklamaState.reklama.set()


@dp.message_handler(IsAdmin(), state=ReklamaState.reklama, content_types=['text', 'photo', 'video', 'audio', 'file'])
async def send_reklama(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    print(message)
    for user in users:
        user_id = user[0]
        if message.photo:
            await bot.send_photo(chat_id=user_id, photo=message.photo[-1].file_id, caption=message.caption)
        elif message.video:
            await bot.send_video(chat_id=user_id, video=message.video.file_id, caption=message.caption)
        else:
            await bot.send_message(chat_id=user_id, text=message)
        await asyncio.sleep(0.05)
    
    await state.finish()


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")