import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config_reader import config
import handlers as h
from crud_functions import initiate_db

api = config.bot_token.get_secret_value()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()

dp.message_handler(commands="start")(h.regular.start)
dp.message_handler(text='Рассчитать')(h.regular.main_menu)
dp.callback_query_handler(text='formulas')(h.regular.get_formulas)
dp.message_handler(text='Купить')(h.regular.get_buying_list)
dp.callback_query_handler(text='product_buying')(h.regular.send_confirm_message)
dp.message_handler(commands='clear_all')(h.regular.clear_all)

dp.callback_query_handler(text='calories')(h.calories.calories_inline)
dp.message_handler(text='calories')(h.calories.calories)
dp.callback_query_handler(state=h.calories.UserState.sex)(h.calories.set_sex)
dp.message_handler(state=h.calories.UserState.age)(h.calories.set_age)
dp.message_handler(state=h.calories.UserState.growth)(h.calories.set_growth)
dp.message_handler(state=h.calories.UserState.weight)(h.calories.set_weight)

dp.message_handler(text='Регистрация')(h.registration.sing_up)
dp.message_handler(state=h.registration.RegistrationState.username)(h.registration.set_username)
dp.message_handler(state=h.registration.RegistrationState.email)(h.registration.set_email)
dp.message_handler(state=h.registration.RegistrationState.age)(h.registration.set_age)

dp.message_handler()(h.regular.all_message)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(dp, allowed_updates=["message", "edited_channel_post", "callback_query", "edited_message",
    #                                             "channel_post", "edited_channel_post", "inline", "chosen_inline",
    #                                             "shipping_query", "pre_checkout_query", "poll", "poll_answer",
    #                                             "my_chat_member", "chat_member", "chat_join_request", "errors", ])
