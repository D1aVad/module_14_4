import asyncio

import crud_functions
import kb
from aiogram.types import InputMediaPhoto, Message
from aiogram.utils.exceptions import MessageToDeleteNotFound


async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb.start_kb)


async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb.inline_kb)


async def get_formulas(call):
    await call.message.answer(
        "Формулы расчета:\n"
        "для мужчин - 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
        "для женщин - 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )
    await call.answer()


async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for id_product, title, description, price in products:
        with open(f'image/image{id_product}.png', "rb") as img:
            text = f"Название: {title} | Описание: {description} | Цена: {price}"
            await message.answer_photo(img, text)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb.product_inline_kb)


async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


async def clear_all(message):
    from main import bot
    count = 1
    message_id = message.message_id
    user_id = message.from_user.id
    while count < 20:
        try:
            await bot.delete_message(user_id, message_id)
            message_id -= 1
            count = 1
        except MessageToDeleteNotFound:
            message_id -= 1
            count += 1


async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")
