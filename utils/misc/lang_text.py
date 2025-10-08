from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from data.config import ADMINS
from keyboards.default.Student_DB import lang_uz_main_m, lang_ru_main_m, uz_management_list, ru_management_list, \
    main_menu_uz, main_menu_ru, back_uz, back_ru
from keyboards.inline.student_IB import confirmation_uz, confirmation_ru
from loader import bot, db
from datetime import datetime
import pytz

from states.states import SendFile
from utils.misc.student_list import get_students_keyboard_ru, get_students_keyboard_uz


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
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"Murojaat matni:\n<i><b>{text_}</b></i>\n\n Murojaat yuboruvchi:\n{call.from_user.mention}")
    text = 'Sizning murojaatingiz "Anonim"ligingizni saqlagan holda masul shaxsga yuborildi✅'
    await call.message.answer(text=text, reply_markup=main_menu_uz)
    await db.add_appeal(user_id=str(call.from_user.id), message=text_, created_at=tashkent_time.replace(tzinfo=None))


async def ru_conf_appeals(call: CallbackQuery, text_):
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)
    await bot.send_message(chat_id=ADMINS[1],
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
            " \t<i><b>Истамов Бекзодбек Бахриддинович</b></i>\n\n")
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


async def student_name_uz(msg):
    text_ = "O'zingizni F.I.SH tanlang!👇"
    msg_ = await msg.answer("...", reply_markup=back_uz)
    await msg_.delete()
    await msg.answer(text=text_, reply_markup=get_students_keyboard_uz(page=0))


async def student_name_ru(msg):
    text_ = "Выберите своё Ф.И.О! 👇"
    msg_ = await msg.answer("...", reply_markup=back_ru)
    await msg_.delete()
    await msg.answer(text=text_, reply_markup=get_students_keyboard_ru(page=0))


async def file_theme_uz(msg: Message, student):
    text = f"Hurmatli {student} siz yubormoqchi bo'lgan hujjat mavzusini kiriting👇"
    await msg.answer(text=text, reply_markup=back_uz)
    await SendFile.theme.set()


async def file_theme_ru(msg: Message, student):
    text = f"Уважаемый(ая) {student}, введите тему документа, который вы хотите отправить 👇"
    await msg.answer(text=text, reply_markup=back_ru)
    await SendFile.theme.set()


async def theme_next_uz(msg: Message, theme):
    text = f"🔰<b><i>{theme}</i></b> ushbu mavzudagi hujjatingizni yuboring👇"
    await msg.answer(text=text, reply_markup=back_uz)


async def theme_next_ru(msg: Message, theme):
    text = f"🔰<b><i>{theme}</i></b> Отправьте ваш документ по этой теме👇"
    await msg.answer(text=text, reply_markup=back_ru)


async def conf_file_uz(msg: Message, state: FSMContext):
    data = await state.get_data()
    theme = data['theme']
    file_id = data["file_id"]
    student = data['student']
    msg_ = await msg.answer("...", reply_markup=back_ru)
    await msg_.delete()
    text = (f"🔰 Hujjat Mavzusi: {theme}\n\n"
            f"🎓 Talaba: {student}")
    await msg.answer_document(document=file_id, caption=text, reply_markup=confirmation_uz)


async def conf_file_ru(msg: Message, state: FSMContext):
    data = await state.get_data()
    theme = data['theme']
    file_id = data["file_id"]
    student = data['student']
    msg_ = await msg.answer("...", reply_markup=back_ru)
    await msg_.delete()
    text = (f"🔰 Тема документа: {theme}\n\n"
            f"🎓 Студент: {student}")
    await msg.answer_document(document=file_id, caption=text, reply_markup=confirmation_ru)


async def conf_photo_uz(msg: Message, state: FSMContext):
    data = await state.get_data()
    theme = data['theme']
    file_id = data["file_id"]
    student = data['student']
    msg_ = await msg.answer("...", reply_markup=back_ru)
    await msg_.delete()
    text = (f"🔰 Hujjat Mavzusi: {theme}\n\n"
            f"🎓 Talaba: {student}")
    await msg.answer_photo(photo=file_id, caption=text, reply_markup=confirmation_uz)


async def conf_photo_ru(msg: Message, state: FSMContext):
    data = await state.get_data()
    theme = data['theme']
    file_id = data["file_id"]
    student = data['student']
    msg_ = await msg.answer("...", reply_markup=back_ru)
    await msg_.delete()
    text = (f"🔰 Тема документа: {theme}\n\n"
            f"🎓 Студент: {student}")
    await msg.answer_photo(photo=file_id, caption=text, reply_markup=confirmation_ru)


async def uz_conf_document(call: CallbackQuery, state: FSMContext):
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)

    data = await state.get_data()
    theme = data['theme']
    file_id = data['file_id']
    student = data['student']
    file_type = data['file_type']

    if file_type == 'photo':
        await bot.send_photo(
            chat_id=ADMINS[0],
            photo=file_id,
            caption=f"Hujjat mavzusi: <i><b>{theme}</b></i>\n"
                    f"Talaba: <i><b>{student}</b></i>\n\n"
                    f"Yuboruvchi: {call.from_user.mention}"
        )

    elif file_type == 'document':
        await bot.send_document(
            chat_id=ADMINS[0],
            document=file_id,
            caption=f"Hujjat mavzusi: <i><b>{theme}</b></i>\n"
                    f"Talaba: <i><b>{student}</b></i>\n\n"
                    f"Yuboruvchi: {call.from_user.mention}"
        )

    text = "Sizning hujjatingiz ma'sul shaxsga yuborildi✅"
    await call.message.answer(text=text, reply_markup=main_menu_uz)

    await db.add_document(
        user_id=str(call.from_user.id),
        theme=theme,
        file_id=file_id,
        file_type=file_type,
        created_at=tashkent_time.replace(tzinfo=None)
    )


async def ru_conf_document(call: CallbackQuery, state: FSMContext):
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)

    data = await state.get_data()
    theme = data['theme']
    file_id = data['file_id']
    student = data['student']
    file_type = data['file_type']

    if file_type == 'photo':
        await bot.send_photo(
            chat_id=ADMINS[0],
            photo=file_id,
            caption=f"📄 Тема документа: <i><b>{theme}</b></i>\n"
                    f"🎓 Студент: <i><b>{student}</b></i>\n\n"
                    f"Отправитель: {call.from_user.mention}"
        )

    elif file_type == 'document':
        await bot.send_document(
            chat_id=ADMINS[0],
            document=file_id,
            caption=f"📄 Тема документа: <i><b>{theme}</b></i>\n"
                    f"🎓 Студент: <i><b>{student}</b></i>\n\n"
                    f"Отправитель: {call.from_user.mention}"
        )

    text = "Ваш документ был отправлен ответственному лицу ✅"
    await call.message.answer(text=text, reply_markup=main_menu_ru)

    await db.add_document(
        user_id=str(call.from_user.id),
        theme=theme,
        file_id=file_id,
        file_type=file_type,
        created_at=tashkent_time.replace(tzinfo=None)
    )
