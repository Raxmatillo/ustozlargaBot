from aiogram.dispatcher.filters.state import State, StatesGroup



class LotinKiril(StatesGroup):
    startLotinKiril = State()


class Translate(StatesGroup):
    startTranslate = State()