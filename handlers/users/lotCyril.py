from aiogram import types 
from aiogram.dispatcher import FSMContext
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
        await message.answer("lotin kiriil yakunlandi")
        await state.finish()
    else:
        if message.text[0] in lotin_kril.latin:
            await message.answer(lotin_kril.ToCyrilic(message.text))
        elif message.text[0] in lotin_kril.cyrilic:
            await message.answer(lotin_kril.ToLatin(message.text))
        else:
            await message.reply('Iltimos matn kiriting☹️')

    
