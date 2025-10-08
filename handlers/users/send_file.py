from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp, db
from states.states import SendFile
from utils.misc.lang_text import student_name_uz, student_name_ru, file_theme_uz, file_theme_ru, uz_text_1, ru_text_1, \
    theme_next_uz, theme_next_ru, conf_file_uz, conf_file_ru, again_write_uz, uz_conf_appeals, uz_conf_document, \
    ru_conf_document, conf_photo_uz, conf_photo_ru
from utils.misc.student_list import get_students_keyboard_uz, get_students_keyboard_ru


@dp.message_handler(text=['⬅️Ortga', "⬅️Назад"], state=SendFile.theme)
async def back_student(msg: Message, state: FSMContext):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await student_name_uz(msg)
    else:
        await student_name_ru(msg)
    await SendFile.student_list.set()


@dp.message_handler(text=['⬅️Ortga', "⬅️Назад"], state=SendFile.send_file)
async def back_theme(msg: Message, state: FSMContext):
    date = await state.get_data()
    student = date['student']
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await file_theme_uz(msg, student)
    else:
        await file_theme_ru(msg, student)
    await SendFile.theme.set()


@dp.callback_query_handler(text='conf', state=SendFile.send_file)
async def confirmation_appeals(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await uz_conf_document(call, state=state)
    else:
        await ru_conf_document(call, state=state)
    await state.finish()


@dp.callback_query_handler(text='again', state=SendFile.send_file)
async def again(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await student_name_uz(call.message)
    else:
        await student_name_uz(call.message)
    await SendFile.student_list.set()


@dp.message_handler(text=["📂Hujjat yuborish", "📂Отправить документ"])
async def send_file(msg: Message, state: FSMContext):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await student_name_uz(msg)
    else:
        await student_name_ru(msg)
    await SendFile.student_list.set()


@dp.callback_query_handler(Text(startswith='page:'), state=SendFile.student_list)
async def change_page(call: CallbackQuery):
    page = int(call.data.split(":")[1])
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await call.message.edit_reply_markup(reply_markup=get_students_keyboard_uz(page))
    else:
        await call.message.edit_reply_markup(reply_markup=get_students_keyboard_ru(page))


@dp.callback_query_handler(Text(startswith="student:"), state=SendFile.student_list)
async def select_student(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    student = call.data.split(":")[1]
    await state.update_data(
        {
            "student": student
        }
    )
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await file_theme_uz(call.message, student)
    else:
        await file_theme_ru(call.message, student)
    await SendFile.theme.set()


@dp.callback_query_handler(text='back_menu', state=SendFile.student_list)
async def back_to_menu_student(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await uz_text_1(call.message)
    else:
        await ru_text_1(call.message)
    await state.finish()


@dp.message_handler(state=SendFile.theme)
async def theme(msg: Message, state: FSMContext):
    await state.update_data(
        {
            "theme": msg.text
        }
    )
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await theme_next_uz(msg, msg.text)
    else:
        await theme_next_ru(msg, msg.text)
    await SendFile.send_file.set()


@dp.message_handler(content_types=["document"], state=SendFile.send_file)
async def file(msg: Message, state: FSMContext):
    file_id = msg.document.file_id
    await state.update_data({
        'file_id': file_id,
        'file_type': 'document'
    })
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await conf_file_uz(msg, state)
    else:
        await conf_file_ru(msg, state)


@dp.message_handler(content_types=["photo"], state=SendFile.send_file)
async def photo(msg: Message, state: FSMContext):
    file_id = msg.photo[-1].file_id
    await state.update_data({
        'file_id': file_id,
        'file_type': "photo"
    })
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await conf_photo_uz(msg, state)
    else:
        await conf_photo_ru(msg, state)
