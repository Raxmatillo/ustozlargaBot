import asyncio
import logging
from filters import IsAdmin
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.dashboardKeyboard import admin_keyboards
from aiogram.utils import exceptions
from keyboards.default.menuKeyboard import cancel
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(IsAdmin(), state="*", text="❌ Bekor qilish")
async def stop_state(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Amaliyot bekor qilindi", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(IsAdmin(), text="/admin")
async def admin_panel(message: types.Message):  
    await message.answer("Siz adminpaneldasiz!", reply_markup=admin_keyboards)

@dp.message_handler(IsAdmin(), text="📌 Reklama")
async def send_ad_to_all(message: types.Message, state: FSMContext):
    await message.answer("Menga reklamani yuboring ...")
    await message.answer("Reklama postini yuboring", reply_markup=cancel)
    await state.set_state("send_ads")



async def send_post(chat_id, message_id, user_id, reply_markup=None):
    try:
        if reply_markup:
            await bot.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=message_id,reply_markup=reply_markup)
        else:
            await bot.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=message_id)
    except exceptions.BotBlocked:
        logging.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        logging.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        logging.error(
            f"Target [ID:{user_id}]: Flood limit is exceeded. "
            f"Sleep {e.timeout} seconds."
        )
        await asyncio.sleep(e.timeout)
        return await bot.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=message_id)
    except exceptions.UserDeactivated:
        logging.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False


@dp.message_handler(IsAdmin(), state="send_ads", content_types=["photo", "video", "text"])
async def send_ads(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    for user in users:
        await send_post(chat_id=ADMINS[0], message_id=message.message_id, user_id=user[1])
        await asyncio.sleep(0.05)
    await bot.send_message(chat_id=message.from_user.id, text="Reklama muvaffaqiyatli yuborildi ✅", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(IsAdmin(), text="📊 Statistika")
async def show_statistics(message: types.Message):
    count = db.count_users()
    await message.answer(f"<b>Botda foydalanuvchilar soni: {count[0]} ta</b>")