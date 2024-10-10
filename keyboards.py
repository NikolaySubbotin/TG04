from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Обычная клавиатура с кнопками "Привет" и "Пока"
main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Привет"), KeyboardButton(text="Пока"),
        ],
    ],
    resize_keyboard=True
)

# Инлайн-клавиатура с ссылками
inline_keyboard_test = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://dzen.ru/news")],
        [InlineKeyboardButton(text="Видео", url="https://yandex.ru/video/search?text=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE")],
        [InlineKeyboardButton(text="Музыка", url="https://vk.com/vkmusic")],
    ]
)

# Инлайн-кнопка "Показать больше"
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ]
)

# Функция для показа новых кнопок "Опция 1" и "Опция 2"
async def show_options():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
            [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
        ]
    )
    return keyboard
