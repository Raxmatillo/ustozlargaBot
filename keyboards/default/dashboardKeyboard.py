from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📌 Reklama")
        ]
    ], resize_keyboard=True
)