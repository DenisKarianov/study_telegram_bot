from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6578683615:AAHviIwc0llgJLFvH3j1OGSYnp29MoBKQP8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть приложение', web_app=WebAppInfo(url='https://aiogram.dev/')))
    await message.answer('Добро пожаловать!', reply_markup=markup)



# @dp.message_handler(content_types=['photo'])  # commands=['start']
# async def start(message: types.Message):
#     # await bot.send_message(message.chat.id, 'Hello!')
#     # await message.answer('Hello, human!')
#     await message.reply('Hi!')
#
#
# @dp.message_handler(commands=['inline'])
# async def info(message: types.Message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Site', url='https://aiogram.dev/'))
#     markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
#     await message.reply('Hello!', reply_markup=markup)
#
#
# @dp.callback_query_handler()
# async def callback(call):
#     await call.message.answer(call.data)
#
#
# @dp.message_handler(commands=['reply'])
# async def reply(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add(types.KeyboardButton('Site'))
#     markup.add(types.KeyboardButton('Hello'))
#     await message.answer('Hello!', reply_markup=markup)


executor.start_polling(dp)
# bot.polling(none_stop=True)