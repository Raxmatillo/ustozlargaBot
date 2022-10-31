from aiogram.dispatcher.filters.state import State, StatesGroup



class SendMessageToAdmin(StatesGroup):
    message = State()


class LotinKiril(StatesGroup):
    startLotinKiril = State()


class Translate(StatesGroup):
    startTranslate = State()