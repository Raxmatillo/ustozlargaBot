from aiogram import types
from aiogram.dispatcher import FSMContext
from states.MyState import Translate
from aiogram.dispatcher.filters import Command
from googletrans import Translator

from loader import dp

translator = Translator()


@dp.message_handler(lambda message: message.text.startswith(('/en', '/ru', '/uz', '/ar', '/de', '/ko', '/tr', '!en', '!ru', '!uz', '!ar', '!de', '!ko', '!tr')))
async def to_eng(message: types.Message):
    if len(message.text) > 3 and message.text[3:]:  # agar matn '/en' dan keyin alifbo bilan boshlansa
        lang = message.text[1:3]
        sentence = message.text[3:].strip()
    else:
        await message.answer('Yordam uchun /help buyrug\'ini yuboring')
        return
    translated_text = translator.translate(sentence, src='auto', dest=lang)
    src = translated_text.src
    word = translated_text.text
    translated_text_ = translator.translate(word, src=src, dest=src)
    pronunciation = translated_text_.pronunciation
    if pronunciation is not None and pronunciation != word:
        pronunciation_text = f"\n<b>Talaffuz: </b> {pronunciation}"
    else: pronunciation_text=''
    await message.reply(f"<b>Tarjima: </b>{word}{pronunciation_text}")