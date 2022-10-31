from aiogram import types 
from aiogram.dispatcher import FSMContext
from states.MyState import LotinKiril, SendMessageToAdmin
from utils.misc import lotinKiril as lotin_kril
from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(text="📝 Xabar yuborish")
async def get_user_message(message: types.Message):
    await message.answer("❗️ <i>Shikoyat/taklif matnini kiriting ...</i>")
    await SendMessageToAdmin.message.set()


@dp.message_handler(state=SendMessageToAdmin.message, content_types="text")
async def send_to_admin(message: types.Message):
    await message.answer("ℹ️ Tashakkur! Xabaringiz adminga yuborildi")
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=message.text, disable_web_page_preview=True)

@dp.message_handler(state=SendMessageToAdmin.message, content_types=["photo", "video", "audio", "file"])
async def unknown_command(message: types.Message):
    await message.answer("Iltimos, matn ko'rinishida yuboring !")

@dp.message_handler(text="🔁 Xatosiz o'girish")
async def bot_echo_lotinKiril(message: types.Message):
    await message.answer("Matn kiriting ....")
    # await LotinKiril.startLotinKiril.set()

@dp.message_handler()
async def convert(message: types.Message, ):
    if message.text[0] in lotin_kril.latin:
        await message.answer(lotin_kril.ToCyrilic(message.text))
    elif message.text[0] in lotin_kril.cyrilic:
        await message.answer(lotin_kril.ToLatin(message.text))
    else:
        await message.reply('Iltimos matn kiriting☹️')

    
