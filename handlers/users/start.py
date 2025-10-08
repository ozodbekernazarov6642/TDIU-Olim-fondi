from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, CallbackQuery
from loader import dp, db
from keyboards.inline.student_IB import lang
from utils.misc.lang_text import uz_text_1, ru_text_1
from datetime import datetime
import pytz


@dp.message_handler(CommandStart(), state='*')
async def start(msg: Message, state: FSMContext):
    user = await db.select_user(str(msg.from_user.id))
    if not user:
        await msg.answer(
            "Assalomu aleykum hurmatli foydalanuvchi!\n"
            "Botdan foydalanish uchun tilni tanlang🤳\n"
            "-----------------------------------------------\n"
            "Здравствуйте, уважаемый студент.\n"
            "Выберите язык для использования бота🤳",
            reply_markup=lang
        )
        return

    lang_code = user.get('language', 'uz')
    if lang_code == 'uz':
        await uz_text_1(msg)
    else:
        await ru_text_1(msg)
    await state.finish()

@dp.callback_query_handler(Text(startswith='lang'))
async def first_step(call: CallbackQuery):
    tz = pytz.timezone("Asia/Tashkent")
    tashkent_time = datetime.now(tz)
    await call.message.delete()
    await db.add_user(
        id=str(call.from_user.id),
        full_name=call.from_user.full_name,
        username=call.from_user.username,
        date_time=tashkent_time.replace(tzinfo=None),
        language=(call.data.split(':')[1])
    )
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await uz_text_1(call.message)
    else:
        await ru_text_1(call.message)
