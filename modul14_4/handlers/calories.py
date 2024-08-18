from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import kb


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


async def calories_inline(call):
    await call.message.answer("Выберите свой пол:", reply_markup=types.ReplyKeyboardRemove())
    await call.message.answer(text='...', reply_markup=kb.sex_kb)
    await call.answer()
    await UserState.sex.set()


async def calories(message):
    await message.answer("Выберите свой пол:", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text='...', reply_markup=kb.sex_kb)
    await UserState.sex.set()


async def set_sex(call, state):
    await call.answer()
    if call.data not in ["Мужчина", "Женщина"]:
        await call.message.answer("Выберите свой пол КНОПКАМИ:", reply_markup=kb.sex_kb)
    else:
        await call.message.edit_text(f"Вы {call.data}")
        await state.update_data(sex=call.message.text)
        await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
        await UserState.age.set()


async def set_age(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой возраст ЦИФРАМИ:")
    else:
        await state.update_data(age=message.text)
        await message.answer("Введите свой рост:")
        await UserState.growth.set()


async def set_growth(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой рост ЦИФРАМИ:")
    else:
        await state.update_data(growth=message.text)
        await message.answer("Введите свой вес:")
        await UserState.weight.set()


async def set_weight(message, state):
    if not message.text.isdigit():
        await message.answer("Введите свой вес ЦИФРАМИ:")
    else:
        await state.update_data(weight=message.text)
        data = await state.get_data()
        s = data['sex']
        w, g, a = map(int, (data["weight"], data["growth"], data["age"]))
        if s == 'Мужчина':
            result = 10 * w + 6.25 * g - 5 * a + 5  # Для мужчин
        else:
            result = 10 * w + 6.25 * g - 5 * a - 161  # Для женщин
        await message.answer(f'Ваша норма калорий в сутки {result:.2f}', reply_markup=kb.start_kb)
        await state.finish()
