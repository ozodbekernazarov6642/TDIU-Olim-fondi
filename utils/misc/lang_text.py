from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from data.config import ADMINS
from keyboards.default.Student_DB import lang_uz_main_m, lang_ru_main_m, uz_management_list, ru_management_list, \
    main_menu_uz, main_menu_ru, back_uz, back_ru
from keyboards.inline.student_IB import confirmation_uz, confirmation_ru
from loader import bot, db
from datetime import datetime
import pytz


async def uz_text_1(msg: Message):
    text = ("🏠Asosiy Menyu\n\n"
            "Kerakli bo'limni tanlang👇")
    await msg.answer(text=text, reply_markup=lang_uz_main_m)


async def ru_text_1(msg: Message):
    text = "🏠Главное меню\n\nВыберите нужный раздел👇"
    await msg.answer(text=text, reply_markup=lang_ru_main_m)


async def uz_management_info(msg: Message):
    text = ("👤Rahbariyat\n\n"
            "Kerakli bo'limni tanlang👇")
    await msg.answer(text=text, reply_markup=uz_management_list)


async def ru_management_info(msg: Message):
    text = ("👤Руководство\n\n"
            "Выберите нужный раздел👇")
    await msg.answer(text=text, reply_markup=ru_management_list)


async def uz_appeals(msg: Message):
    text = "Xurmatli talaba siz o'z murojaatingizni yozib qoldiring👇"
    await msg.answer(text=text, reply_markup=back_uz)


async def ru_appeals(msg: Message):
    text = "Уважаемый студент, пожалуйста, оставьте своё обращение👇"
    await msg.answer(text=text, reply_markup=back_ru)


async def uz_appeals_conf(msg: Message):
    text = (f"<b><i>{msg.text}</i></b>\n\n"
            f"Murojaat matningiz tog'riligini tekshiring!")
    await msg.answer(text=text, reply_markup=confirmation_uz, parse_mode='HTML')


async def ru_appeals_conf(msg: Message):
    text = (f"<b><i>{msg.text}</i></b>\n\n"
            f"Пожалуйста, проверьте правильность вашего обращения!")
    await msg.answer(text=text, reply_markup=confirmation_ru, parse_mode='HTML')


async def uz_conf_appeals(call: CallbackQuery, text_):
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Murojaat matni:\n<i><b>{text_}</b></i>\n\n Murojaat yuboruvchi:\n{call.from_user.mention}")
    text = 'Sizning murojaatingiz "Anonim"ligingizni saqlagan holda masul shaxsga yuborildi✅'
    await call.message.answer(text=text, reply_markup=main_menu_uz)
    await db.add_appeal(user_id=str(call.from_user.id), message=text_, created_at=tashkent_time.replace(tzinfo=None))


async def ru_conf_appeals(call: CallbackQuery, text_):
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Текст обращения:\n<i><b>{text_}</b></i>\n\n Отправитель обращения:\n{call.from_user.mention}")
    text = 'Ваше обращение было отправлено ответственному лицу с сохранением анонимности✅'
    await call.message.answer(text=text, reply_markup=main_menu_ru)
    await db.add_appeal(user_id=str(call.from_user.id), message=text_, created_at=tashkent_time.replace(tzinfo=None))


async def again_write_uz(call: CallbackQuery):
    text = "Aha ho'p😊 Bemalol murojaatingizni qayta yozishingiz mumkin✍️"
    await call.message.answer(text=text)


async def again_write_ru(call: CallbackQuery):
    text = "Конечно😊 Вы можете спокойно переписать своё обращение✍️"
    await call.message.answer(text=text)


async def fond_rah_uz(msg: Message):
    text = ("🔰Fond rahbari\n"
            " \t<i><b>Istamov Bekzodbek Bahriddinovich</b></i>\n\n")
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_uz)


async def fond_rah_ru(msg: Message):
    text = ("🔰Руководитель фонда\n"
            " \t<i><b>Истамов Бекзодбек Бахриддинович</b></i>\n\n"
            )
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_ru)


async def kuz_keng_rais_uz(msg: Message):
    text = ("🔰Kuzatuv kengashi raisi\n"
            " \t<i><b>Istamov Bekzodbek Bahriddinovich</b></i>\n\n")
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_uz)


async def kuz_keng_raisi_ru(msg: Message):
    text = ("🔰Председатель наблюдательного совета\n"
            " \t<i><b>Истамов Бекзодбек Бахриддинович</b></i>\n\n"
            )
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_ru)


async def cordinator_uz(msg: Message):
    text = ("🔰Koordinator\n"
            " \t<i><b>Istamov Bekzodbek Bahriddinovich</b></i>\n\n")
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_uz)


async def cordinato_ru(msg: Message):
    text = ("🔰Координатор\n"
            " \t<i><b>Истамов Бекзодбек Бахриддинович</b></i>\n\n"            )
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_uz)


async def expert_uz(msg: Message):
    text = ("🔰Ekspert\n"
            " \t<i><b>Istamov Bekzodbek Bahriddinovich</b></i>\n\n")
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_uz)


async def expert_ru(msg: Message):
    text = ("🔰Эксперт\n"
            " \t<i><b>Истамов Бекзодбек Бахриддинович</b></i>\n\n"
            )
    await msg.answer_photo(photo="AgACAgIAAxkBAAIK5WjhkvFVN3eFH7hIXHGc3_6bksNjAAJN-DEbtHEJS8Ecb2txQNXBAQADAgADeQADNgQ",
                           caption=text, reply_markup=main_menu_uz)


async def change_lang_text_uz(msg: Message):
    text = "Til muvoffaqqiyatli o'zgartirildi✅"
    await msg.answer(text=text, reply_markup=ReplyKeyboardRemove())


async def change_lang_text_ru(msg: Message):
    text = "Язык успешно изменен✅"
    await msg.answer(text=text, reply_markup=ReplyKeyboardRemove())
