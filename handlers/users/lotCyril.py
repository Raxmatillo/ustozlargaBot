from aiogram import types 
from aiogram.dispatcher import FSMContext
from handlers.users.admin import send_ad_to_all, show_statistics
from handlers.users.faq import get_user_message
from handlers.users.tarjimon import start_translate
from states.MyState import LotinKiril, SendMessageToAdmin
from utils.misc import lotinKiril as lotin_kril
from data.config import ADMINS
from loader import dp, bot

@dp.message_handler(text="🔁 Xatosiz o'girish")
async def bot_echo_lotinKiril(message: types.Message):
    await message.answer("Matn kiriting ....")
    await LotinKiril.startLotinKiril.set()

@dp.message_handler(state=LotinKiril.startLotinKiril)
async def convert(message: types.Message, state: FSMContext):
    if message.text in ["📝 Xabar yuborish", "🔁 Xatosiz o'girish", "🌐 Tarjima qiling", "📌 Reklama", "📊 Statistika"]:
        await state.finish()
        if message.text == "📝 Xabar yuborish":
            await get_user_message(message)
        elif message.text == "🔁 Xatosiz o'girish":
            await bot_echo_lotinKiril(message)
        elif message.text == "🌐 Tarjima qiling":
            await start_translate(message)
        elif message.text == "📌 Reklama":
            await send_ad_to_all(message)
        elif message.text == "📊 Statistika":
            await show_statistics(message)
        else:
            await bot_echo_lotinKiril(message)
    else:
        if message.text[0] in lotin_kril.latin:
            await message.answer(lotin_kril.ToCyrilic(message.text))
        elif message.text[0] in lotin_kril.cyrilic:
            await message.answer(lotin_kril.ToLatin(message.text))
        else:
            await message.reply('Iltimos xarif bilan boshlanuvchi matn kiriting☹️')

    
