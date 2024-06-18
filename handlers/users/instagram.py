import logging
from aiogram import types
from loader import dp
from states.states import Insta
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands='link')
async def insta(message: types.Message):
    await message.answer('havola yuboring: ')
    await Insta.yukla.set()


@dp.message_handler(state=Insta.yukla)
async def step1(message: types.Message, state:FSMContext):
    link = message.text[12:]
    await message.answer_video(f"https://dd{link}", caption="Video yuklab olindi")