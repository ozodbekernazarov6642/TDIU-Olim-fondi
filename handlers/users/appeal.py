from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp, db
from states.states import AppealStates
from utils.misc.lang_text import uz_appeals, ru_appeals, uz_appeals_conf, ru_appeals_conf, uz_conf_appeals, \
    ru_conf_appeals, again_write_uz, again_write_ru, uz_text_1, ru_text_1


@dp.message_handler(text=["✍️️Murojaat yuborish", "✍️Отправить обращение"])
async def appeal(msg: Message, state: FSMContext):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await uz_appeals(msg)
    else:
        await ru_appeals(msg)
    await AppealStates.writing.set()


@dp.message_handler(state=AppealStates.writing)
async def writing_appeals(msg: Message, state: FSMContext):
    await state.update_data({'text_': msg.text})
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await uz_appeals_conf(msg)
    else:
        await ru_appeals_conf(msg)


@dp.callback_query_handler(text='conf', state=AppealStates.writing)
async def confirmation_appeals(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await uz_conf_appeals(call, text_=data['text_'])
    else:
        await ru_conf_appeals(call, text_=data['text_'])
    await state.finish()


@dp.callback_query_handler(text='again', state=AppealStates.writing)
async def again(call: CallbackQuery):
    await call.message.delete()
    if (await db.select_user(str(call.from_user.id)))['language'] == 'uz':
        await again_write_uz(call)
    else:
        await again_write_ru(call)
