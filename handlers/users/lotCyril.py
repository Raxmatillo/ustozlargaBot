from aiogram import types 
from aiogram.dispatcher import FSMContext
from states.MyState import LotinKiril
from utils.misc import lotinKiril as lotin_kril

from loader import dp

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