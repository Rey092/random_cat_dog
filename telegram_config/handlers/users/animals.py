import random
from aiogram import types
from aiogram.dispatcher.filters import Text

from telegram_config.loader import dp, bot

from serpapi import GoogleSearch


def get_image(keyword):
    params = {
      "q": f"{keyword}",
      "tbm": "isch",
      "ijn": "0",
      "api_key": "4f3f102b27bacd2bcd0ed7dace8019227090b7cf39c8c8d39034120867c4f7a9"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']
    i = random.randrange(len(images_results))
    image_url = images_results[i]['original']
    return image_url


@dp.message_handler(Text('Котики'))
async def bot_echo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=get_image('милый кот'))


@dp.message_handler(Text('Собачки'))
async def bot_echo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=get_image('милый щенок'))


@dp.message_handler(Text('Зайчики'))
async def bot_echo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=get_image('милый зайчик'))
