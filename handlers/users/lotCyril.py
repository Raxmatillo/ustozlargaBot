from aiogram import types 
from aiogram.dispatcher import FSMContext
from utils.misc import lotinKiril as lotin_kril

from loader import dp


@dp.message_handler()
async def convert(message: types.Message, state: FSMContext):
    if message.text[0] in lotin_kril.latin:
        await message.answer(lotin_kril.ToCyrilic(message.text))
    elif message.text[0] in lotin_kril.cyrilic:
        await message.answer(lotin_kril.ToLatin(message.text))

    
