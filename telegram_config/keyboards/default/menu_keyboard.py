from aiogram import types


def get_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["Котики", "Собачки", "Зайчики"]
    keyboard.add(*buttons)
    return keyboard
