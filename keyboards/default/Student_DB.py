from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


lang_uz_main_m = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤Rahbariyat"),
            KeyboardButton(text="✍️️Murojaat yuborish")
        ],
        [
          KeyboardButton(text="📂Hujjat yuborish")
        ],
        [
            KeyboardButton(text="🇺🇿Tilni o'zgartish🇷🇺")
        ]
    ], resize_keyboard=True
)

lang_ru_main_m = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤Руководство"),
            KeyboardButton(text="✍️Отправить обращение")
        ],
        [
            KeyboardButton(text="📂Отправить документ")
        ],
        [
            KeyboardButton(text="🇷🇺Изменить язык🇺🇿")
        ]
    ], resize_keyboard=True
)

uz_management_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💼 Fond rahbari"),
            KeyboardButton(text="🤝 Koordinator"),
        ],
        [
            KeyboardButton(text="👔 Kuzatuv kengashi raisi"),
            KeyboardButton(text="🧠 Ekspert")
        ],
        [
            KeyboardButton(text="⬅️Ortga")
        ]
    ], resize_keyboard=True
)

ru_management_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💼 Руководитель фонда"),
            KeyboardButton(text="🤝 Координатор"),
        ],
        [
            KeyboardButton(text="👔 Председатель наблюдательного совета"),
            KeyboardButton(text="🧠 Эксперт")
        ],
        [
            KeyboardButton(text="⬅️Назад")
        ]
    ], resize_keyboard=True
)

main_menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Bosh Menyu")
        ]
    ], resize_keyboard=True
)

main_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)

back_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️Ortga")
        ]
    ], resize_keyboard=True
)

back_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️Назад")
        ]
    ],resize_keyboard=True
)
