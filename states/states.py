from aiogram.dispatcher.filters.state import StatesGroup, State

class Insta(StatesGroup):
    yukla = State()

class Dowload(StatesGroup):
    dowload = State()

class AI(StatesGroup):
    talk = State()