from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

students = [f"Talaba {i}" for i in range(1, 31)]


def get_students_keyboard_uz(page: int = 0):
    per_page = 10
    start = page * per_page
    end = start + per_page
    markup = InlineKeyboardMarkup(row_width=2)

    for student in students[start:end]:
        markup.add(InlineKeyboardButton(text=student, callback_data=f"student:{student}"))

    nav_buttons = [InlineKeyboardButton(text="🔙", callback_data="back_menu")]
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️", callback_data=f"page:{page - 1}"))
    if end < len(students):
        nav_buttons.append(InlineKeyboardButton(text="➡️", callback_data=f"page:{page + 1}"))

    if nav_buttons:
        markup.row(*nav_buttons)

    return markup


def get_students_keyboard_ru(page: int = 0):
    per_page = 10
    start = page * per_page
    end = start + per_page
    markup = InlineKeyboardMarkup(row_width=2)

    for student in students[start:end]:
        markup.add(InlineKeyboardButton(text=student, callback_data=f"student:{student}"))

    nav_buttons = [InlineKeyboardButton(text="🔙", callback_data="back_menu")]
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page:{page - 1}"))
    if end < len(students):
        nav_buttons.append(InlineKeyboardButton(text="➡️ Далее", callback_data=f"page:{page + 1}"))

    if nav_buttons:
        markup.row(*nav_buttons)

    return markup
