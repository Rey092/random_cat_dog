from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from telegram_config.keyboards.default.menu_keyboard import get_menu_keyboard
from telegram_config.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=get_menu_keyboard())