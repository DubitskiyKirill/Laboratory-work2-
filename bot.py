from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import Parser
import debug
import time
#from main import collect_data
from config import TOKEN
def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def process_start_command(msg: types.Message):
        start_buttons = ["Ввод границ", "Помощь"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*start_buttons)
        await bot.send_message(msg.from_user.id,
                               "Здравствуйте!\nМеня зовут Рублик, я - бот, который отправляет уведомления, при выходе курса доллара за заданные границы.",
                               reply_markup=keyboard)
        await bot.send_message(msg.from_user.id,
                               "Пожалуйста, введите верхнюю и нижнюю границу, при которых необходимо отправить уведомление.")

    @dp.message_handler(Text(equals="Помощь"))
    async def process_help_command(msg: types.Message):
        help_buttons = ["Ввод границ"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*help_buttons)
        await bot.send_message(msg.from_user.id,
                               "Я слежу за курсом доллара и отправляю Вам уведомление, если он выходит за заданную границу.",
                               reply_markup=keyboard)

    @dp.message_handler(Text(equals="Ввод границ"))
    async def process_help_command(msg: types.Message):
        print(debug.current_datetime, msg.from_user.username, '=', msg.text)
        await msg.reply(
            "Введите границы через пробел, начиная с нижней, отделив дробную часть точкой. К примеру, 80.92")
        high_buttons = ["Помощь"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*high_buttons)

        @dp.message_handler(content_types=types.ContentType.TEXT)
        async def check_number(msg: types.Message):
            try:
                znac = 1.
                while True:
                    time.sleep(60)
                    Parser.parse()
                    num1, num2 = map(float, msg.text.split())
                    if ((num2 <= Parser.msg1) or (num1 >= Parser.msg1)) and (Parser.msg1 != znac):
                        znac = Parser.msg1
                        await bot.send_message(msg.from_user.id,
                                               "Внимание! Курс доллара вышел за заданные границы! Курс доллара: " + str(
                                                   znac))
            except ValueError:
                await bot.send_message(msg.from_user.id, "Неверный формат чисел. Введите два числа через пробел.")

    executor.start_polling(dp)