from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация'), ],
        [KeyboardButton(text="Купить"),],
        [KeyboardButton(text="Регистрация"),],
    ], resize_keyboard=True
)


inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(callback_data="calories", text="Рассчитать норму калорий", ),
         InlineKeyboardButton(callback_data="formulas", text="Формулы расчёта", )],
    ]
)


sex_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(callback_data="Мужчина", text="Мужчина"),
         InlineKeyboardButton(callback_data="Женщина", text="Женщина")],
    ],
)


buy_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Купить"),],
    ], resize_keyboard=True
)


product_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(callback_data="product_buying", text="Продукт 1", ),
         InlineKeyboardButton(callback_data="product_buying", text="Продукт 2", ),
         InlineKeyboardButton(callback_data="product_buying", text="Продукт 3", ),
         InlineKeyboardButton(callback_data="product_buying", text="Продукт 4", ), ],
    ]
)
