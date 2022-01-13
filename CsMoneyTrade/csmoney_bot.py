import json
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
from config import token


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Ножи"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Выберите категорию", reply_markup=keyboard)


@dp.message_handler(Text(equals="Ножи"))
async def get_discount_knives(message: types.Message):
    await message.answer("Please waiting...")

    collect_data()

    with open("result.json", encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item["full_name"], item["3d"])}\n' \
            f'{hbold("Скидка: ")}{item["overprice"]}%\n' \
            f'{hbold("Цена: ")}{item["price"]}$'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
