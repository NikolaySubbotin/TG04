import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart, Command

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Старт", reply_markup=kb.main)

@dp.message(F.text == "Привет")
async def hello(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def bye(message: Message):
    await message.answer(f"Пока, {message.from_user.first_name}!")

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer("Ссылки", reply_markup=kb.inline_keyboard_test)


# Команда /dynamic для инлайн-кнопки "Показать больше"
@dp.message(Command('dynamic'))
async def show_more_button(message: Message):
    await message.answer("Нажми на кнопку, чтобы показать больше опций:", reply_markup=kb.keyboard)


# Обработчик нажатия на кнопку "Показать больше"
@dp.callback_query(F.data == "show_more")
async def show_more(callback: CallbackQuery):
    await callback.message.edit_text("Выберите опцию:", reply_markup=await kb.show_options())

# Обработчик для кнопки "Опция 1"
@dp.callback_query(lambda call: call.data == "option_1")
async def option_1_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 1")

# Обработчик для кнопки "Опция 2"
@dp.callback_query(lambda call: call.data == "option_2")
async def option_2_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 2")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
