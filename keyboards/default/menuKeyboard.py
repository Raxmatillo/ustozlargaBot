from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔁 Xatosiz o'girish"),
            KeyboardButton(text="🌐 Tarjima qiling")
        ]
    ], resize_keyboard=True
)