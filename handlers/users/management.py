from aiogram.types import Message
from loader import dp, db
from utils.misc.lang_text import uz_management_info, ru_management_info, fond_rah_uz, fond_rah_ru, kuz_keng_rais_uz, \
    kuz_keng_raisi_ru, cordinator_uz, cordinato_ru, expert_uz, expert_ru


@dp.message_handler(text=['👤Rahbariyat', "👤Руководство"])
async def management_info(msg: Message):
    user = await db.select_user(str(msg.from_user.id))
    if user['language'] == 'uz':
        await uz_management_info(msg)
    else:
        await ru_management_info(msg)


@dp.message_handler(text=['💼 Fond rahbari', '💼 Руководитель фонда'])
async def fond_rah(msg: Message):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await fond_rah_uz(msg)
    else:
        await fond_rah_ru(msg)


@dp.message_handler(text=['👔 Kuzatuv kengashi raisi', '👔 Председатель наблюдательного совета'])
async def kuzatuv_kengashi(msg: Message):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await kuz_keng_rais_uz(msg)
    else:
        await kuz_keng_raisi_ru(msg)


@dp.message_handler(text=['🤝 Koordinator', '🤝 Координатор'])
async def koordinator(msg: Message):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await cordinator_uz(msg)
    else:
        await cordinato_ru(msg)


@dp.message_handler(text=['🧠 Ekspert', '🧠 Эксперт'])
async def ekspert(msg: Message):
    if (await db.select_user(str(msg.from_user.id)))['language'] == 'uz':
        await expert_uz(msg)
    else:
        await expert_ru(msg)
