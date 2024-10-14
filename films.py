import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN, OMDB_API_KEY  # Убедитесь, что OMDB_API_KEY есть в вашем config.py

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Функция для получения данных о фильме
def get_film_data(title: str):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    response = requests.get(url)

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            return None
    return None


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Напиши мне название фильма, и я пришлю тебе постер и описание.")


@dp.message()
async def send_film_info(message: Message):
    film_title = message.text
    film_data = get_film_data(film_title)

    if film_data:
        title = film_data.get("Title")
        year = film_data.get("Year")
        plot = film_data.get("Plot")
        poster_url = film_data.get("Poster")

        response_text = f"Название фильма: {title}\n  Год: {year}\n  Описание: {plot}"

        # Отправляем постер, если он есть
        if poster_url and poster_url != "N/A":
            await message.answer_photo(photo=poster_url, caption=response_text)
        else:
            await message.answer(response_text)
    else:
        await message.answer("Не удалось найти фильм с таким названием. Попробуйте другое.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
